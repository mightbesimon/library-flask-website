''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, session, request

from ..adapters import _repo
from ..handlers import nav, authorisation, useronly, ReviewForm, SearchTitleForm, SearchForm
from ..models   import Review


blueprint = Blueprint('catalogue', __name__)


@blueprint.route('/catalogue', methods=['GET', 'POST'])
def catalogue():
    form = SearchTitleForm()

    if form.validate_on_submit():
        return redirect(f'/catalogue/search?title={form.title.data}') \
            if form.title.data else redirect('/catalogue/search')

    return render_template('catalogue.html', nav=nav,
        catalogue=_repo.get_catalogue(), form=form)


@blueprint.route('/catalogue/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    print(form.data)

    if form.validate_on_submit():
        args = {
            'title'    : form.title,
            'author'   : form.author,
            'year'     : form.year,
            'publisher': form.publisher
        }
        query = '&'.join( f'{label}={field.data}' 
                          for label, field in args.items() 
                          if field.data and field.data!='<ANY>' )
        return redirect(f'/catalogue/search?{query}')

    # url query string
    title     = request.args.get('title'    )
    author    = request.args.get('author'   )
    year      = request.args.get('year'     )
    publisher = request.args.get('publisher')

    # match functions dictionary
    match_dictionary = {
        title : lambda book: title.lower() in book.title.lower(),
        author: lambda book: any(author==a.full_name for a in book.authors),
        year  : lambda book: int(year)==book.release_year,
        publisher: lambda book: publisher==book.publisher.name
    }

    match = lambda book: all(func(book)
                for arg, func in match_dictionary.items() if arg)
    catalogue = _repo.get_books(function=match)

    return render_template('catalogue.html', nav=nav,
        catalogue=catalogue, form=form)


@blueprint.route('/book/<bookID>')
def book(bookID):
    book = _repo.get_book(book_id=int(bookID))
    user = _repo.get_current_user()
    reviews = _repo.get_reviews(book=book)
    return render_template('book_info.html', nav=nav,
        book=book, reviews=reviews, user=user, form=None)


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
    reviews = _repo.get_reviews(book=book)
    form = ReviewForm()

    if not form.validate_on_submit():
        return render_template('book_info.html', nav=nav,
            book=book, reviews=reviews, user=user, form=form)

    review = Review(book, user, form.review_text.data, int(form.rating.data))
    user.add_review(review)
    _repo.add_review(review)
    return redirect(f'/book/{bookID}')
