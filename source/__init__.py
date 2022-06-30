"""
This contains the application factory for creating flask application instances.
Using the application factory allows for the creation of flask applications configured
for different environments based on the value of the CONFIG_TYPE environment variable
"""

import os

from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login.login_manager import LoginManager
from flask_sqlalchemy import SQLAlchemy

# from config import basedir

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    """ App factory function """

    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    # Initialize App Database objects
    initialize_database(app)

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    initialize_extensions(app)

    # Configure logging
    # configure_logging(app)

    # Register error handlers
    # register_error_handlers(app)

    return app

### Helper Functions ###
def register_blueprints(app):
    """ Registering all blueprint in app instances """
    from source.user import auth_blueprint
    from source.main import main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/users')
    app.register_blueprint(main_blueprint)

def initialize_database(app):
    """ Initializing databases """
    db.init_app(app)
    migrate.init_app(app, db)

def initialize_extensions(app):
    """ Initializing third party extensions """
    mail.init_app(app)
    login_manager.login_view="user.login"
    login_manager.login_message_category="info"
    login_manager.init_app(app)

# def register_error_handlers(app):
#     """ App level error handling """
#     pass


# def configure_logging(app):
#     """ Configuration of logging feature """
#     pass
