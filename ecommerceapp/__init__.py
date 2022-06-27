"""Initialize E-Commerce app."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login.login_manager import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view="login"
    login_manager.login_message_category="info"
    login_manager.init_app(app)
    
    with app.app_context():
        from ecommerceapp import routes  # Import routes
        db.create_all()  # Create database tables for our data models
        return app