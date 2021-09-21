''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, session

from ..adapters import _repo
from ..handlers import nav, authorisation, useronly


blueprint = Blueprint('catalogue', __name__)


@blueprint.route('/catalogue')
def catalogue():
    return render_template('catalogue.html', nav=nav, catalogue=_repo.get_catalogue())

@blueprint.route('/book/<bookID>')
def book(bookID):
    book = _repo.get_book(book_id=int(bookID))
    user = _repo.get_current_user()
    return render_template('book_info.html', nav=nav, book=book, user=user)

@blueprint.route('/book/<bookID>/read')
@authorisation(useronly)
def read(bookID):
    book = _repo.get_book(book_id=int(bookID))
    user = _repo.get_current_user()
    if book in user.read_books:
        user.read_books.remove(book)
    else:
        user.read_a_book(book)
    return redirect(f'/book/{bookID}')

# @blueprint.route('/book/<bookID>/review')
# @authorisation(useronly)
# def review(bookID):
#     return render_template('book_review.html', nav=nav, book=)
