from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import profile, login, signup, search, createBoard