"""Flask configuration variables."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECURITY_PASSWORD_SALT = environ.get("SECURITY_PASSWORD_SALT")

    # Database
    SQLALCHEMY_DATABASE_URI = f"mysql://{environ.get('USER')}:{environ.get('PASSWORD')}@{environ.get('HOST')}/{environ.get('DATABASE')}"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False