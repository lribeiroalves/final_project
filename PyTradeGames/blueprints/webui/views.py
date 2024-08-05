"""Creation of the views to registered on the webui blueprint"""

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, RegisterForm

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import *


# HOMEPAGE
def index():
    return render_template('homepage/index.html')


# USER INTERFACE
@login_required
def profile():
    return render_template('homepage/profile.html')


def add_games():
    games = db.session.execute(db.select(Games)).scalars()
    return render_template('homepage/games.html', games = games)


# AUTHENTIFICATION
def login():
    if current_user.is_authenticated:
        flash('User already autenticated.')
        return redirect(url_for('webui.index'))

    form = LoginForm()
    
    if form.validate_on_submit():
        user = db.session.execute(db.select(Users).filter_by(username=form.username.data)).scalar()
        
        if not check_password_hash(user.password, form.password.data):
            flash('User or password Incorrect.')
            return redirect(url_for('webui.login'))
        else:
            login_user(user)
            flash(f'User has logged in successfully.')

            next_request = form.next.data
            return redirect(next_request) if next_request != 'None' else redirect(url_for('webui.index'))

    next = request.args.get('next')
    
    return render_template('auth/login.html', form=form, next=next)


@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('User logged out.')

    return redirect(url_for('webui.index'))


def register():
    if current_user.is_authenticated:
        flash('User already autenticated.')
        return redirect(url_for('webui.index'))

    form = RegisterForm()
    
    if form.validate_on_submit():
        new_user = Users()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.password = generate_password_hash(form.password.data)
        new_user.admin = False

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successfull.')

        return redirect(url_for('webui.login'))

    return render_template('auth/register.html', form=form)
