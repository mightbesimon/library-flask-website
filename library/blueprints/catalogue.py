''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, url_for

from ..adapters import _repo
from ..handlers import nav


blueprint = Blueprint('catalogue', __name__)


@blueprint.route('/catalogue')
def catalogue():
    return render_template('catalogue.html', nav=nav, catalogue=_repo.get_catalogue())

@blueprint.route('/book/<bookID>')
def book(bookID):
    return render_template('book_info.html', nav=nav, book=_repo.get_book(book_id=int(bookID)))

@blueprint.route('/')
def home():
    return redirect(url_for('catalogue.catalogue'))
