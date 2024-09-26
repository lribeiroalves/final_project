"""CLI Commands Factory"""

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Genres, Maker, Consoles, Trades
from .population_data import *
import click
from werkzeug.security import generate_password_hash


def create_db():
    """Creates the Database"""
    db.create_all()
    click.echo('Database Initialized.')


def drop_db():
    """Drop the entire database"""
    db.drop_all()
    click.echo("Droped the entire database")


def populate_db():
    """Creates data for development only using population_data file"""
    makers = create_makers()
    db.session.add_all(makers)
    makers_query = db.session.execute(db.select(Maker)).scalars().all()
    
    consoles = create_consoles(makers_query=makers_query)
    db.session.add_all(consoles)
    consoles_query = db.session.execute(db.select(Consoles)).scalars().all()

    genres = create_genres()
    db.session.add_all(genres)
    genres_query = db.session.execute(db.select(Genres)).scalars().all()

    games = create_games(genres_query=genres_query, consoles_query=consoles_query)
    db.session.add_all(games)
    games_query = db.session.execute(db.select(Games)).scalars().all()

    users = create_users(games_query=games_query)
    db.session.add_all(users)
    
    db.session.commit()
    click.echo('Database populated.')



def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))