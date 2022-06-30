""" Main app views"""
from . import main_blueprint
from flask import render_template, request, redirect, url_for

@main_blueprint.route('/home')
@main_blueprint.route('/')
def home():
    print("Dev")
    """ Home Page Views"""
    return render_template('home.html')
