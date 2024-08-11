"""Webui blueprint factory"""

from flask import Blueprint

from .views import *

bp = Blueprint('webui', __name__)

bp.add_url_rule('/', view_func=index)
bp.add_url_rule('/profile', view_func=profile)
bp.add_url_rule('/games', view_func=games)
bp.add_url_rule('/add_game', methods=['POST'], view_func=add_game)
bp.add_url_rule('/users', view_func=users)
bp.add_url_rule('/start_trade', methods=['POST'], view_func=start_trade)
bp.add_url_rule('/trades/<int:trade_id>', view_func=trade)
bp.add_url_rule('/auth/login', methods=['GET', 'POST'], view_func=login)
bp.add_url_rule('/auth/logout', methods=['GET', 'POST'], view_func=logout)
bp.add_url_rule('/auth/register', methods=['GET', 'POST'], view_func=register)


def init_app(app):
    app.register_blueprint(bp)