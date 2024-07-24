from flask import render_template
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users

from .forms import LoginForm, RegisterForm


def index():
    return render_template('homepage/index.html')


def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = db.session.execute(db.select(Users).filter_by(username=form.username.data)).scalar()
        print('logged in')
        # criar a logica de validação de usuario e senha

    return render_template('auth/login.html', form=form)


def logout():
    return 'logout view'


def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        print('registered')

    return render_template('auth/register.html', form=form)