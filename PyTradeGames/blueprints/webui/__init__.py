from flask import Blueprint

from .views import index, login

bp = Blueprint('webui', __name__)

bp.add_url_rule('/', view_func=index)
bp.add_url_rule('/login', methods=['GET', 'POST'], view_func=login)


def init_app(app):
    app.register_blueprint(bp)