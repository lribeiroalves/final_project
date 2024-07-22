from flask import render_template

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Maker

from .forms import LoginForm


def index():
    return render_template('base.html')


def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        return 'Success!'

    return render_template('auth/login.html', form=form)