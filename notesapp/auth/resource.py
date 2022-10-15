from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from notesapp.models import User

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
                flash("Logged in successfully", category="success")
                return redirect(url_for("views.home"))

    return render_template("login.html")


@auth.route("/auth/recover-password")
def recover_password():
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
