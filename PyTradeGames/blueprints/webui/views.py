from flask import render_template
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users

from .forms import LoginForm, RegisterForm


def index():
    return render_template('base.html')


def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = db.session.execute(db.select(Users).filter_by(username=form.username.data)).scalar()
        # criar a logica de validação de usuario e senha

    return render_template('auth/login.html', form=form)


def logout():
    return 'logout view'


def register():
    form = RegisterForm()
    
    return 'register view'