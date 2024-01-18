from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("homepage.html")

@views.route("/about")
def about():
    return render_template("just a test")

@views.route("portfolio")
def portfolio():
    return render_template("just a test")

@views.route("skills")
def skills():
    return render_template("just a test")


@views.route("contact")
def contact():
    return render_template("just a test")



