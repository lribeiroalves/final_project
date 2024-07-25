"""Webui blueprint factory"""

from flask import Blueprint

from .views import index, login, logout, register

bp = Blueprint('webui', __name__)

bp.add_url_rule('/', view_func=index)
bp.add_url_rule('/auth/login', methods=['GET', 'POST'], view_func=login)
bp.add_url_rule('/auth/logout', methods=['GET', 'POST'], view_func=logout)
bp.add_url_rule('/auth/register', methods=['GET', 'POST'], view_func=register)


def init_app(app):
    app.register_blueprint(bp)