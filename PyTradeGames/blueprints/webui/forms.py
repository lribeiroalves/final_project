import re
from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, ValidationError


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

    pattern = re.compile('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$')

    def _email_check(form, field):
        email = field.data

        user = db.session.execute(db.select(Users).filter_by(email=email)).scalar()

        if user is not None:
            raise ValidationError('Email address already on database.')
        else:
            if not pattern.match(email):
                raise ValidationError('Invalid email address.')
    
    return _email_check


def password_check():
    """Password Validation for Registration Form"""

    def _password_check(form, field):
        password = field.data
        
    
    return _password_check


# FORMS
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), user_exist()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), user_taken()])
    email = EmailField('Email', validators=[DataRequired(), ])