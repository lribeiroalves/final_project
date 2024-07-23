from flask_login import LoginManager, AnonymousUserMixin

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(Users).filter_by(id = user_id)).scalar()


class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.admin = False


def init_app(app):
    login_manager.init_app(app)
    login_manager.login_view = 'webui.login'
    login_manager.session_protection = "strong"
    login_manager.anonymous_user = Anonymous
