''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from ..adapters import _repo


class ValidateUsername:

    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        if _repo.username_exists(field.data):
            raise ValidationError(self.message)


class ValidatePassword:

    def __init__(self, message1, message2, message3):
        self.message1 = message1
        self.message2 = message2
        self.message3 = message3

    def __call__(self, form, field):
        if not any(c.isdigit() for c in field.data):
            # raise ValidationError(self.message1)
            field.errors.append(self.message1)
        if not any(c.isupper() for c in field.data):
            # raise ValidationError(self.message2)
            field.errors.append(self.message2)
        if not any(c.islower() for c in field.data):
            # raise ValidationError(self.message3)
            field.errors.append(self.message3)


class RegistrationForm(FlaskForm):

    username = StringField('Username', [
        DataRequired(message='A username is required for registration 😅'),
        Length(min=6, message='That username is too short 😅'),
        ValidateUsername(message='That username is taken 😅 do you want to login?'),
    ])
    password = PasswordField('Password', [
        DataRequired(message='A password is required for registration 😅'),
        Length(min=6, message='That password is too short 😅'),
        ValidatePassword(
            message1='Your password needs a digit 😅',
            message2='Your password needs an upper case character 😅',
            message3='Your password needs a lower case character 😅',
        ),
    ])
    submit = SubmitField('Register')
