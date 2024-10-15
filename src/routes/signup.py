from . import routes
from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
import flask
import flask_login
from src.app import get_db
from src.models.user import user_loader, request_loader, User, find_user, create_user

@routes.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        if not (username and password and email):
            return render_template("sign-up.html", message="All fields are required.")

        if find_user(email):
            return render_template("sign-up.html", message="This email is already associated with an account!")
        
        create_user(email, username, password)

        return redirect("login")
    return render_template("sign-up.html")





