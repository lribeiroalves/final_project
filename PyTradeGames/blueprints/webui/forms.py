"""Creation of forms to be used on webui."""

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, HiddenField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

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