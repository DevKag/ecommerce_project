""" Main app views"""
from flask import render_template
from . import main_blueprint


@main_blueprint.route('/home')
@main_blueprint.route('/')
def home():
    """ Home Page Views"""
    return render_template('home.html')
