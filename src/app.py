import os
import datetime
from flask import Flask, render_template, request, redirect, url_for, g, session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from flask_login import LoginManager
from pprint import pprint

def db_connect():
    load_dotenv()
    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    db_name = os.getenv('MONGO_DBNAME')

    if not all([username, password, db_name]):
        raise ValueError("Missing MongoDB credentials in .env file")
    
    uri = f"mongodb+srv://{username}:{password}@cluster0.lrz8n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        raise

    return client[db_name]

def get_db():
    if 'db' not in g:
        g.db = db_connect()
    return g.db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.secret_key = os.getenv('SECRET_KEY')
    login_manager.init_app(app)
    register_blueprint(app)

    with app.app_context():
        get_db()
    
    return app

def register_blueprint(app):
    from src.routes import routes
    app.register_blueprint(routes)



