""" Main app views"""
from flask import render_template, request
from . import main_blueprint


@main_blueprint.route('/home')
@main_blueprint.route('/')
def home():
    """ Home Page Views"""
    next_page = request.args.get("next")
    # return redirect(next_page) if next_page else redirect(url_for('main.home'))
    return render_template('home.html')
