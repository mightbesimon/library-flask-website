''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, session

from ..adapters import _repo
from ..handlers import nav, authorisation, useronly, ReviewForm
from ..models   import Review


blueprint = Blueprint('catalogue', __name__)


@blueprint.route('/catalogue')
def catalogue():
    return render_template('catalogue.html', nav=nav, catalogue=_repo.get_catalogue())

@blueprint.route('/book/<bookID>')
def book(bookID):
    book = _repo.get_book(book_id=int(bookID))
    user = _repo.get_current_user()
    return render_template('book_info.html', nav=nav, book=book, user=user, form=None)

@blueprint.route('/book/<bookID>/read')
@authorisation(policy=useronly)
def read(bookID):
    book = _repo.get_book(book_id=int(bookID))
    user = _repo.get_current_user()
    if book in user.read_books:
        user.read_books.remove(book)
    else:
        user.read_a_book(book)
    return redirect(f'/book/{bookID}')

@blueprint.route('/book/<bookID>/review', methods=['GET', 'POST'])
@authorisation(policy=useronly)
def review(bookID):
    book = _repo.get_book(book_id=int(bookID))
    user = _repo.get_current_user()
    form = ReviewForm()

    if not form.validate_on_submit():
        return render_template('book_info.html', nav=nav, book=book, user=user, form=form)

    review = Review(book, form.review_text.data, int(form.rating.data))
    user.add_review(review)
    _repo.add_review(review)
    return redirect(f'/book/{bookID}')
