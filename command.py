""" File to define all deployment configuration"""
import click

from flask import Blueprint
from flask.cli import with_appcontext
from flask_migrate import upgrade, migrate, init, stamp

from source.user.models import User, UserType, Gender
from source import db 

admin_bp = Blueprint('admin',__name__, cli_group=None)


@admin_bp.cli.command("create_db")
@with_appcontext
def create_db():
    """ Creating databases """
    # click.echo("Database created")
    db.create_all()
    init()
    stamp()
    migrate()
    upgrade()


@admin_bp.cli.command("migrate")
@with_appcontext
def migrate_db():
    """ Migrating Database """
    migrate()
    upgrade()


@admin_bp.cli.command("drop_db")
@with_appcontext
def drop_db():
    """ Drop whole Databases """
    db.session.commit()
    db.drop_all()


@admin_bp.cli.command("adminuser")
@with_appcontext
def create_user():
    """ Create Database User """
    print(" Please Enter your admin users Details ")
    name = click.prompt("Enter username")
    email = click.prompt("Enter email", type=str)
    password  = click.prompt("Enter Password", type=str)
    user      = User(lastname=name, firstname=name, dob= None, address=None, email=email,
                    password=password, usertype=UserType.ADMIN, gender=Gender.MALE, confirmed=True, approval=True)
    db.session.add(user)
    db.session.commit()
