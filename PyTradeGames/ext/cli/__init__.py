"""CLI Commands Factory"""

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Genres, Maker, Consoles, Trades
import click
from werkzeug.security import generate_password_hash
import datetime


def create_db():
    """Creates the Database"""
    db.create_all()
    click.echo('Database Initialized.')


def drop_db():
    """Drop the entire database"""
    db.drop_all()
    click.echo("Droped the entire database")


def populate_db():
    """Creates data for development only"""
    makers = [
        Maker(name = 'Sony'),
        Maker(name = 'Microsoft'),
        Maker(name = 'Nintendo'),
        Maker(name = 'Sega')
    ]
    db.session.add_all(makers)
    makers_query = db.session.execute(db.select(Maker)).scalars().all()
    
    consoles = [
        Consoles(name = 'PS3', maker = makers_query[0]),
        Consoles(name = 'PS4', maker = makers_query[0]),
        Consoles(name = 'XBOX 360', maker = makers_query[1]),
    ]
    db.session.add_all(consoles)
    consoles_query = db.session.execute(db.select(Consoles)).scalars().all()

    genres =[
        Genres(genre = 'Adventure'),
        Genres(genre = 'Horror'),
        Genres(genre = 'RPG'),
    ]
    db.session.add_all(genres)
    genres_query = db.session.execute(db.select(Genres)).scalars().all()

    games = [
        Games(name='The Elder Scrolls V - Skyrim', genres = [genres_query[0], genres_query[2]], consoles = [c for c in consoles_query]),
        Games(name='InFamous', genres = [genres_query[0]], consoles = [consoles_query[0]]),
    ]
    db.session.add_all(games)
    games_query = db.session.execute(db.select(Games)).scalars().all()

    users = [
        Users(username = 'admin', email = 'admin@admin.com', password = generate_password_hash('Admin@Py_Trade_Games'), admin = True, since = datetime.datetime.now()),
        Users(username = 'lribeiro', email = 'lucasribeiroalves@live.com', password = generate_password_hash('Flask@2024'), admin = False, games = [g for g in games_query], since = datetime.datetime.now()),
        Users(username = 'seduarte', email = 'selma@hotmail.com', password = generate_password_hash('Flask@2024'), admin = False, games = [games_query[1]], since = datetime.datetime.now()),
    ]
    db.session.add_all(users)
    
    db.session.commit()
    click.echo('Database populated.')



def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))