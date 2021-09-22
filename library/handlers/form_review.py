''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

from ..adapters import _repo


class ReviewForm(FlaskForm):

    rating = RadioField('Your rating', choices=[1,2,3,4,5], validators=[
        DataRequired(message='A rating is required for a review 😅'),
    ])
    review_text = TextAreaField('Your review')
    submit = SubmitField('Post')
