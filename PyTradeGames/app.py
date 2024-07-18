"""Creation and managing of the app, app settings and app factory."""

from flask import Flask

from .ext import configuration
from .ext import database
from .ext import commands

app = Flask(__name__)


configuration.init_app(app)
database.init_app(app)
commands.init_app(app)


@app.route('/')
def index():
    return str(app.config.get("TITLE"))