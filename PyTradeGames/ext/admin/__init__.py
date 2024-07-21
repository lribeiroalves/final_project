from flask_admin import Admin
from .views import UserAdmin, GameAdmin, ConsoleAdmin, GenreAdmin, MakerAdmin
from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Consoles, Genres, Makers


def init_app(app):
    admin = Admin(app, 'PyTradeGames', template_mode='bootstrap3')
    admin.add_view(UserAdmin(Users, db.session))
    admin.add_view(GameAdmin(Games, db.session))
    admin.add_view(GenreAdmin(Genres, db.session))
    admin.add_view(ConsoleAdmin(Consoles, db.session))
    admin.add_view(MakerAdmin(Makers, db.session))