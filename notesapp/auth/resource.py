import os
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from notesapp.models import ResetPassword, User
from notesapp import mail
from flask_mail import Message
auth = Blueprint("auth", __name__)


@auth.route("/auth/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Please enter all fields", category="danger")
        else:
            user = User.query.filter_by(email=email).first()
            if not user:
                flash("User does not exist", category="danger")
            elif not User.verify_password(password, user.password):
                flash("Incorrect password", category="danger")
            else:
                login_user(user, remember=True)
                # flash("Logged in successfully", category="success")
                return redirect(url_for("views.home"))

    return render_template("login.html")


@auth.route("/auth/recover-password", methods=["GET", "POST"])
def recover_password():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        email = request.form.get("email")
        if not email:
            flash("Please enter all fields", category="danger")
        else:
            user = User.query.filter_by(email=email).first()
            if not user:
                flash("User does not exist", category="danger")
            else:
                msg = Message("Password Recovery", sender=os.environ.get("MAIL_USERNAME"), recipients=[email])
                token = ResetPassword.generate_token(email)
                link = f"{request.url_root}auth/reset-password/{token}"
                msg.body = f"Hi {user.username}, click on the link below to reset your password: \n \
                    {link}"
                mail.send(msg)
                flash("An email has been sent to you with instructions to reset your password", category="success")
                return redirect(url_for("auth.login"))

    return render_template("recover-password.html")


@auth.route("/auth/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not email or not first_name or not password or not confirm_password or not last_name:
            flash("Please enter all fields", category="danger")
        elif password != confirm_password:
            flash("Passwords do not match", category="danger")
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                flash("User already exists", category="danger")
            else:
                new_user = User(
                    email=email,
                    username=first_name + " " + last_name,
                    password=User.generate_hash(password),
                )
                new_user.save()
                flash("Account created please login", category="success")
                return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth.route("/auth/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/auth/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    if request.method == "POST":
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not password or not confirm_password:
            flash("Please enter all fields", category="danger")
        elif password != confirm_password:
            flash("Passwords do not match", category="danger")
        else:
            reset_token = ResetPassword.get_reset_password_token(token)
            if not reset_token:
                flash("Invalid or expired token", category="danger")
            else:
                if reset_token.is_used:
                    flash("Token has been used", category="danger")
                else:
                    if not ResetPassword.verify_token(token):
                        flash("Invalid or expired token", category="danger")
                    else:
                        user = User.query.filter_by(email=reset_token.email).first()
                        user.password = User.generate_hash(password)
                        user.save()
                        reset_token.is_used = True
                        reset_token.save()
                        flash("Password reset successfully", category="success")
                        return redirect(url_for("auth.login"))

    return render_template("reset-password.html")