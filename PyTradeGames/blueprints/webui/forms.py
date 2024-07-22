from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError


# VALIDATORS
def user_exist():
    """Check if the username provided by the user matches an existent user"""

    def _user_exist(form, field):
        username = field.data

        user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()

        if user is None:
            print(user)
            raise ValidationError('User not found.')
        
    return _user_exist

# FORMS
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), user_exist()])
    password = PasswordField('Password', validators=[DataRequired()])