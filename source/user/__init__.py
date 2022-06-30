""" Initilization and Blueprint file for User App"""
from flask import Blueprint

auth_blueprint = Blueprint('user', __name__, template_folder='templates')

from . import views