"""Creation and managing of the app, app settings and app factory."""

from flask import Flask
from .ext import configuration


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    
    @app.route('/')
    def index():
        return 'Hello, World!'

    return app

