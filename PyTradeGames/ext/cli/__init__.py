"""CLI Commands Factory"""

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Genres
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
    """Creates data for development only"""
    user1 = Users(username = 'lucas', password = '1234', email = 'lucasribeiroalves@live.com', country = 'Brazil', games = [Games(name = 'God Of War', genres = [Genres(genre = 'Adventure')]), Games(name = 'The Legend of Zelda')])
    db.session.add(user1)
    games_query = db.session.execute(db.select(Games)).scalars()
    user2 = Users(username = 'selma', password = '1234', email = 'selma@email.com', country = 'Brazil', games = [game for game in games_query])
    db.session.add(user2)
    db.session.commit()
    click.echo('Database populated.')


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))