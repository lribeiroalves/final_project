"""CLI Commands Factory"""

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users
import click


def create_db():
    """Creates the Database"""
    db.create_all()
    click.echo('Database Initialized.')


def drop_db():
    """Drop the entire database"""
    db.drop_all()
    click.echo("Droped the entire database")


def populate_db():
    """Creates data for tests only"""
    data = [
        Users(id = 1, username = 'lucas', password = '1234'),
        Users(id = 2, username = 'selma', password = '1234')
    ]
    db.session.add_all(data)
    db.session.commit()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))