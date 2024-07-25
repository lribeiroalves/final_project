"""Database Migration Factory"""

from flask_migrate import Migrate

from PyTradeGames.ext.database import db


def init_app(app):
    migrate = Migrate(app, db, command='migration')