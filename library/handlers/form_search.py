''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

from ..adapters import _repo


class SearchTitleForm(FlaskForm):

    title = StringField()
    submit = SubmitField('Search')


def get_authors_names():
    names = _repo.get_authors_names().sort()
    names.insert(0, '<ANY>')
    return names

def get_release_years():
    years = _repo.get_release_years() \
                 .remove(None).sort(reverse=True)
    years.insert(0, '<ANY>')
    return years

def get_publishers_names():
    names = _repo.get_publishers_names() \
                 .remove('N/A').sort()
    names.insert(0, '<ANY>')
    return names

class SearchForm(FlaskForm):

    title  = StringField('Title')
    author = SelectField('Author'      , choices=get_authors_names())
    year   = SelectField('Release Year', choices=get_release_years())
    publisher = SelectField('Publisher', choices=get_publishers_names())
    submit = SubmitField('Search')
