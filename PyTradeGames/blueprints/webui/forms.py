"""Creation of forms to be used on webui."""

from flask_login import current_user

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Trades

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, HiddenField, IntegerField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.widgets import TextArea

from password_strength import PasswordPolicy, PasswordStats


# CONSTANTS
pw_policy = PasswordPolicy.from_names(
    length=8,
    numbers=1,
    uppercase=1,
    special=1
)


# VALIDATORS
def user_exist():
    """Check if the username provided by the user matches an existent user"""

    def _user_exist(form, field):
        username = field.data

        user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()

        if user is None:
            raise ValidationError('User not found.')
        
    return _user_exist


def user_taken():
    """Check if the username has already been taken"""

    def _user_taken(form, field):
        username = field.data

        user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()

        if user is not None:
            raise ValidationError('Username already taken.')
    
    return _user_taken


def email_check():
    """Check if email address is valid and if it already exists in database"""

    def _email_check(form, field):
        email = field.data

        user = db.session.execute(db.select(Users).filter_by(email=email)).scalar()

        if user is not None:
            raise ValidationError('Email address already on database.')
    
    return _email_check


def password_check():
    """Password Validation for Registration Form"""

    def _password_check(form, field):
        pw = field.data
        
        if len(pw_policy.test(pw)) > 0:
            raise ValidationError(
                """Password doesn't meet the minimum requirements: At least 8 character, 1 number, 1 uppercase letter and 1 special character."""
                )
        elif PasswordStats(pw).strength() < 0.333:
            raise ValidationError("Password too weak!")
    
    return _password_check


def user_check(current=False):
    """ Validation on the user provided by the form
        Checks if the current_user matches the user provided
        or if the user provided exists on database """
    
    def _user_check(form, field):
        user_id = int(field.data)

        if current:
            if current_user.id != user_id:
                raise ValidationError("User provided doesn't match the user currently logged in.")
        else:
            user = db.session.execute(db.select(Users).filter_by(id=user_id)).scalar()

            if user is None:
                raise ValidationError("User selected doesn't exist.")
        
    return _user_check


def user_has_game_check(other_field):
    """ Validation on the game provided by the form for the trade. """

    def _user_has_game_check(form, field):
        game = db.session.execute(db.select(Games).filter_by(id=int(field.data))).scalar()
        user = db.session.execute(db.select(Users).filter_by(id=form[other_field].data)).scalar()

        if game is None:
            raise ValidationError("Selected Game doesn't exist.")

        if user is None or game not in user.games:
            raise ValidationError("The selected User doesn't have the selected game.")
    
    return _user_has_game_check


# FORMS
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), user_exist()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField('next')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), user_taken()])
    email = EmailField('Email', validators=[DataRequired(), email_check(), Email(check_deliverability=True, message='Not a valid e-mail address.')])
    password = PasswordField('Password', validators=[DataRequired(), password_check(), EqualTo('confirm_password', message='Password and confirmation must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])


class AddGameForm(FlaskForm):
    game_id = HiddenField('game_id', validators=[DataRequired()])
    game = StringField('Game', validators=[DataRequired()])
    action = HiddenField('action', validators=[DataRequired()])


class StartTradeForm(FlaskForm):
    start_user = HiddenField('start_user_id', validators=[DataRequired(), user_check(current=True)])
    start_game = HiddenField('start_game_id', validators=[DataRequired(), user_has_game_check(other_field='start_user')])
    end_user = HiddenField('end_user_id', validators=[DataRequired(), user_check()])
    end_game = HiddenField('end_game_id', validators=[DataRequired(), user_has_game_check(other_field='end_user')])


class MessageForm(FlaskForm):
    message = StringField('Message', widget=TextArea(), validators=[DataRequired()])


class ReviewForm(FlaskForm):
    message = StringField('Message', widget=TextArea())
    rating = RadioField('Rating', choices=[(i, '★') for i in range(5)], validators=[DataRequired()])
