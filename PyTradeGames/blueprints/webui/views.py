"""Creation of the views to registered on the webui blueprint"""

from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, RegisterForm, AddGameForm, StartTradeForm

from sqlalchemy import or_

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import *

from datetime import datetime


# HOMEPAGE ---------------------------------------------------------------------------------------
def index():
    return render_template('homepage/index.html')


# USER INTERFACE ---------------------------------------------------------------------------------------
@login_required
def profile():
    user_trades = db.session.execute(db.select(Trades).filter(or_(Trades.start_user_id==current_user.id,Trades.end_user_id==current_user.id))).scalars().all()
    
    return render_template('homepage/profile.html', trades=user_trades)


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


@login_required
def start_trade():
    form = StartTradeForm()
    users = db.session.execute(db.select(Users)).scalars()

    if form.validate_on_submit():
        st_user = db.session.execute(db.select(Users).filter_by(id=int(form.start_user.data))).scalar()
        ed_user = db.session.execute(db.select(Users).filter_by(id=int(form.end_user.data))).scalar()
        st_game = db.session.execute(db.select(Games).filter_by(id=int(form.start_game.data))).scalar()
        ed_game = db.session.execute(db.select(Games).filter_by(id=int(form.end_game.data))).scalar()

        new_trade = Trades()
        new_trade.status = 'open'
        new_trade.initial_datetime = datetime.now()
        new_trade.start_user = st_user
        new_trade.start_game = st_game
        new_trade.end_user = ed_user
        new_trade.end_game = ed_game

        db.session.add(new_trade)

        new_msg = Messages()
        new_msg.content = f'Hello {ed_user.username}, i would like to start a trade with you. I offer my {st_game.name} in exchange for your {ed_game.name}. Are you interested?'
        new_msg.date = datetime.now()
        new_msg.from_user = st_user
        new_msg.to_user = ed_user
        new_msg.trade = db.session.execute(db.select(Trades)).scalars().all()[-1]

        db.session.add(new_msg)

        trade_id = db.session.execute(db.select(Trades)).scalars().all()[-1].id
        
        db.session.commit()
        
        flash('New trade created, wait for the other users answer.')
        return redirect(url_for('webui.trade', trade_id=trade_id))
    else:
        return render_template('homepage/users.html', form=form, users=users)


@login_required
def trade(trade_id):
    tr = db.session.execute(db.select(Trades).filter_by(id=trade_id)).scalar()
    print(type(tr))

    if tr is None:
        abort(400, 'Transaction not found.')
    else:
        if current_user != tr.start_user and current_user != tr.end_user:
            abort(400, 'Current User not associated with the selected transaction.')
        else:
            # create here the trade view backend ---------------------------------
            
            return render_template('homepage/trade.html', trade=tr)


# AUTHENTIFICATION ---------------------------------------------------------------------------------------
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
