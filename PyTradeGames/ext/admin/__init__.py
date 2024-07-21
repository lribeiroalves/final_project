from flask_admin import Admin


def init_app(app):
    admin = Admin(app, 'PyTradeGames', template_mode='bootstrap3')