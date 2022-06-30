""" File to define all deployment configuration"""
def deploy():
    """ Run deployment tasks. """
    from flask_migrate import upgrade, migrate, init, stamp
    from source import create_app, db
    from source.user.models import User

    app = create_app()
    app.app_context().push()
    db.create_all()

    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()

deploy()