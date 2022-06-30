""" Flask app Configuration in all environment"""

import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config:
    """
    Base configuration class. Contains default configuration settings
    + configuration settings applicable to all environments.
    """
    # Default settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    # Settings applicable to all environments
    SECRET_KEY = os.environ.get('SECRET_KEY', default='A very terrible secret key.')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='')
    MAIL_SUPPRESS_SEND = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', default=' ')


class DevelopmentConfig(Config):
    """ Defining Development Config """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

class TestingConfig(Config):
    """ Defining Test Config """
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI',
                                default=DevelopmentConfig.SQLALCHEMY_DATABASE_URI)

class ProductionConfig(Config):
    """ Defining Production Config """
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI',
    default=DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
