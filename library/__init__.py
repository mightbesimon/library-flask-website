''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Flask, render_template, redirect, url_for

from config import EnvConfig
from .adapters.LibraryRepository import LibraryRepository


_repo = LibraryRepository()


def create_app():
    app = Flask(__name__)
    app.config.from_object(EnvConfig)

    @app.route('/')
    def home():
        return redirect(url_for('catalogue'))

    @app.route('/catalogue')
    def catalogue():
        return render_template('catalogue.html', catalogue=_repo.get_catalogue())

    @app.route('/book/<bookID>')
    def book(bookID):
        return render_template('book_info.html', book=_repo.get_book(book_id=int(bookID)))

    return app