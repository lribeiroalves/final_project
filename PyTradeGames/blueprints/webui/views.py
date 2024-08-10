"""Creation of the views to registered on the webui blueprint"""

from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, RegisterForm, AddGameForm, StartTradeForm

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import *


# HOMEPAGE
def index():
    return render_template('homepage/index.html')


# USER INTERFACE
@login_required
def profile():
    return render_template('homepage/profile.html')


def games():
    form = AddGameForm()
    games = db.session.execute(db.select(Games)).scalars()

    return render_template('homepage/games.html', games=games, form=form)


@login_required
def add_game():
    form = AddGameForm()
    games = db.session.execute(db.select(Games)).scalars()

    if form.validate_on_submit():
        game_id = int(form.game_id.data)
        game = db.session.execute(db.select(Games).filter_by(id = game_id)).scalar()

        if game is not None:
            my_user = db.session.execute(db.select(Users).filter_by(id=current_user.id)).scalar()
            
            try:
                index = my_user.games.index(game)
            except ValueError:
                index = -1

            if form.action.data == 'add':
                if index < 0:
                    my_user.games.append(game)
                    flash('Game added to your account.')
                else:
                    flash('The current user already has the selected game.')
            elif form.action.data == 'del':
                if index >= 0:
                    my_user.games.pop(index)
                    flash('Game removed from your account.')
                else:
                    flash("The current user doesn't have the selected game. Therefore, is not possible to exclude it.")
            else:
                flash('Action not allowed.')
            db.session.commit()
        else:
            flash('Game Id has not been found.')

    return redirect(url_for('webui.games'))


def users():
    form = StartTradeForm()
    users = db.session.execute(db.select(Users)).scalars()

    return render_template('homepage/users.html', users=users, form=form)


def start_trade():
    form = StartTradeForm()
    users = db.session.execute(db.select(Users)).scalars()

    if form.validate_on_submit():
        print(db.session.execute(db.select(Users).filter_by(id=int(form.start_user.data))).scalar())
        print(db.session.execute(db.select(Games).filter_by(id = int(form.start_game.data))).scalar())
        print(db.session.execute(db.select(Users).filter_by(id=int(form.end_user.data))).scalar())
        print(db.session.execute(db.select(Games).filter_by(id = int(form.end_game.data))).scalar())

        return redirect(url_for('webui.users'))
    else:
        return render_template('homepage/users.html', form=form, users=users)

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
