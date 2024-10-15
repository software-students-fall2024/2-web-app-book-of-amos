from . import routes
from flask import Flask, render_template, request, redirect, url_for, session
import pymongo
from dotenv import load_dotenv
import flask
import flask_login
from src.models.user import user_loader, request_loader
from src.models.user import User
from src.app import get_db
from flask_login import login_required

@routes.route("/",methods=['GET','POST'])
@routes.route("/login",methods=['GET','POST'])
def login():
    users = get_db().users
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    email = flask.request.form['email']
    password = flask.request.form['password']
    result = users.find_one({"email":email, "password":password})
    if result:
        user = User()
        user.id = email
        user.email = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('routes.protected'))

    return 'Bad login'

@routes.route('/protected')
@flask_login.login_required
def protected():
    return flask.redirect('/profile')


@routes.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect("/")