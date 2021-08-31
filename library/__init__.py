''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Flask, render_template

from config import EnvConfig
from library.adapters.LibraryRepository import LibraryRepository


_repo = LibraryRepository()


def create_app():
    app = Flask(__name__)
    app.config.from_object(EnvConfig)

    @app.route('/')
    def home():
        return render_template('catalogue.html', catalogue=_repo.get_catalogue())

    @app.route('/book/<id>')
    def book(id):
        return render_template('simple_book.html', book=_repo.get_book_by_id(id))

    return app