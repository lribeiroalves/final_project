from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from ..database import db
from ..database.models import Users



class UserAdmin(ModelView):
    column_formatters = {
        'username': lambda s, r, u, *a: u.username.capitalize(),
        'games': lambda s, r, u, *a: [game.name for game in u.games]
    }

    column_list = ['username', 'email', 'admin']
    can_edit = False
    can_create = False
    can_delete = False

    @action(
        'toogle_admin',
        'Toogle Admin Status',
        'Are you sure?'
    )
    def toogle_admin(self, ids):
        for user in db.session.execute(db.select(Users).where(Users.id.in_(ids))).scalars():
            user.admin = not user.admin
        db.session.commit()


class GameAdmin(ModelView):
    column_formatters = {
        'users': lambda s, r, g, *a: [user.username for user in g.users]
    }

    column_list = ['name', 'genres', 'consoles']
    form_excluded_columns = ['users']
    can_delete = False


class GenreAdmin(ModelView):
    column_formatters = {
        'games': lambda s, r, g, *a: [game.name for game in g.games]
    }

    form_excluded_columns = ['games']
    can_delete = False


class ConsoleAdmin(ModelView):
    column_formatters = {
        'games': lambda s, r, c, *a: [game.name for game in c.games]
    }

    column_list = ['name', 'maker']
    form_excluded_columns = ['games']
    can_delete = False


class MakerAdmin(ModelView):
    can_delete = False