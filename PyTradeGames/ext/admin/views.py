from flask_admin.contrib.sqla import ModelView
from ..database import db
from ..database.models import Maker

# makers = db.session.execute(db.select(Maker)).scalars()


class UserAdmin(ModelView):
    column_formatters = {
        'username': lambda s, r, u, *a: u.username.capitalize(),
        'games': lambda s, r, u, *a: [game.name for game in u.games]
    }

    column_list = ['username', 'email', 'admin', 'games']
    can_edit = False


class GameAdmin(ModelView):
    column_formatters = {
        'users': lambda s, r, g, *a: [user.username for user in g.users]
    }

    column_list = ['name', 'genres', 'consoles', 'users']


class GenreAdmin(ModelView):
    column_formatters = {
        'games': lambda s, r, g, *a: [game.name for game in g.games]
    }

    column_list = ['genre', 'games']


class ConsoleAdmin(ModelView):
    column_formatters = {
        'games': lambda s, r, c, *a: [game.name for game in c.games]
    }

    column_list = ['name', 'maker', 'games']


class MakerAdmin(ModelView):
    pass