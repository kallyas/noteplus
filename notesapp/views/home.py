from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def redirect_to_home():
    return redirect(url_for("views.home"))

@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", username=current_user.username)