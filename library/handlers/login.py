''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from ..adapters import _repo


class ValidateUsername:

    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        if not _repo.username_exists(field.data):
            raise ValidationError(self.message)


class ValidatePassword:

    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        # if username doesn't exist, then do thing for password
        if form.username.errors:
            return
        # validate password
        if not _repo.authenticate_user(form.username.data, field.data):
            raise ValidationError(self.message)


class LoginForm(FlaskForm):

    username = StringField('Username', [
        DataRequired(message='A username is required for logging in 😅'),
        ValidateUsername(message='That username doesn\'t exist 😅 do you want to register?'),
    ])
    password = PasswordField('Password', [
        DataRequired(message='A password is required for logging in 😅'),
        ValidatePassword(message='Incorrect password 😱'),
    ])
    submit = SubmitField('Let me in')
    question = 'Don\'t have an account yet? Do you want to', 'register', '?'
    url = '/register'
