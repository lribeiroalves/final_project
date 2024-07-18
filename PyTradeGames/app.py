from flask import Flask

from .ext import configuration

app = Flask(__name__)

configuration.init_app(app)

@app.route('/')
def index():
    return str(app.config.get("TITLE"))