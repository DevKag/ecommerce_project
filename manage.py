""" File to define all deployment configuration"""
from flask_migrate import upgrade, migrate, init, stamp
from source import create_app, db


def deploy():
    """ Run deployment tasks. """

    app = create_app()
    app.app_context().push()
    db.create_all()

    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()

deploy()
