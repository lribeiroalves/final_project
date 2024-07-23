from flask import url_for, redirect, request

from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action

from ..database import db
from ..database.models import Users

from flask_login import current_user


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('webui.login', next=request.url))


class UserAdmin(MyModelView):
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


class GameAdmin(MyModelView):
    column_formatters = {
        'users': lambda s, r, g, *a: [user.username for user in g.users]
    }

    column_list = ['name', 'genres', 'consoles']
    form_excluded_columns = ['users']
    can_delete = False


class GenreAdmin(MyModelView):
    column_formatters = {
        'games': lambda s, r, g, *a: [game.name for game in g.games]
    }

    form_excluded_columns = ['games']
    can_delete = False


class ConsoleAdmin(MyModelView):
    column_formatters = {
        'games': lambda s, r, c, *a: [game.name for game in c.games]
    }

    column_list = ['name', 'maker']
    form_excluded_columns = ['games']
    can_delete = False


class MakerAdmin(MyModelView):    
    can_delete = False