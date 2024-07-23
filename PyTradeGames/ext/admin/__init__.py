from flask import redirect, url_for, request
from flask_login import current_user
from flask_admin import Admin, AdminIndexView
from .views import UserAdmin, GameAdmin, ConsoleAdmin, GenreAdmin, MakerAdmin
from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Consoles, Genres, Maker


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('webui.login', next=request.url))


def init_app(app):
    admin = Admin(app, app.config('TITLE'), template_mode='bootstrap3', index_view=MyAdminIndexView())
    admin.add_view(UserAdmin(Users, db.session))
    admin.add_view(GameAdmin(Games, db.session))
    admin.add_view(GenreAdmin(Genres, db.session))
    admin.add_view(ConsoleAdmin(Consoles, db.session))
    admin.add_view(MakerAdmin(Maker, db.session))