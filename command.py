""" File to define all deployment configuration"""
import click
from flask.cli import with_appcontext
from flask_migrate import upgrade, migrate, init, stamp
from source import create_app, db
from source.user.models import User, UserType, Gender


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

# app = create_app()


# @click.command("migrate")
# @with_appcontext
# def create_db():
#     """ Creating databases"""
#     click.echo("Database created")
#     db.create_all()
#     init()
#     stamp()
#     migrate()
#     upgrade()
# app.cli.add_command(create_db)

# @click.command("createuser")
# @click.argument("name")
# @with_appcontext
# def create_user():
#     name = click.prompt("Enter username:", type=str)
#     email = click.prompt("Enter email", type=str)
#     password  = click.prompt("Enter Password", type=str)
#     user      = User(lastname=name, firstname=name, dob= None, address=None, email=email,
#                     password=password, confirmed=True)
#     db.session.add(user)
#     db.session.commit()
# app.cli.add_command(create_user)




