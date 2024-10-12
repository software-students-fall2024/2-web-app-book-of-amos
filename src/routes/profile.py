from . import routes
from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
import flask
import flask_login
from src.models.user import user_loader, request_loader
from src.models.user import User
from src.models.boards import get_boards_by_user, delete_board,duplicate_board

@flask_login.login_required
@routes.route('/profile', methods=["GET", "POST"])
def home():
        if flask.request.method == 'POST':    
            if 'delete' in flask.request.form:
                delete_board(flask.request.form['delete'])
            elif 'duplicate' in flask.request.form:
                 duplicate_board(flask.request.form['duplicate'])
        try:
            boards = get_boards_by_user(flask_login.current_user.email)
            boards = boards.to_list()
        except:
            return flask.redirect('/login')
    
        return(render_template('profile.html', username=flask_login.current_user.username, boards=boards))