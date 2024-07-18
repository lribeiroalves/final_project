from flask import Flask

from .ext.configuration import config

app = Flask(__name__)

config.init_app(app)

@app.route('/')
def index():
    return str(app.config.get("TITLE"))