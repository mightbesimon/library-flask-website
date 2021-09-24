''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from hashlib import sha256
from flask   import session

from .dataset import DataSet
from .irepository import IRepository
from .librarydatacontext import LibraryDataContext

class LibraryRepository(IRepository):

    def __init__(self):
        self._database = LibraryDataContext()

    def username_exists(self, username):
        return self._database.users.any(username=username.lower())

    def add_user(self, user):
        '''returns a copy of the entry added to the database'''
        entry = self._database.users.add(user)
        return entry

    def authenticate_user(self, username, password):
        user = self._database.users.first_or_default(username=username.lower())
        if not user: return False
        salted_hash, salt = user.password.split(':')
        # re-salt-hash the provided password and check if match
        return salted_hash == sha256((salt+password).encode()).hexdigest()

    def get_user(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.users.first_or_default(**kwargs)

    def get_current_user(self):
        return self.get_user(username=session['username']) \
            if 'username' in session else None

    def get_catalogue(self):
        '''get all books in the catalogue'''
        return self._database.catalogue

    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.books.first_or_default(**kwargs)

    def get_reviews(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.reviews.where(*args, **kwargs)

    def add_review(self, review):
        '''returns a copy of the entry added to the database'''
        entry = self._database.reviews.add(review)
        return entry

    def get_authors_names(self):
        '''get all authors' names, no duplicates'''
        return self._database.books.select(lambda book: book.authors) \
                                   .flatten() \
                                   .select(lambda author: author.full_name) \
                                   .remove_dupes()

    def get_release_years(self):
        '''get all release years, no duplicates'''
        return self._database.books.select(lambda book: book.release_year) \
                                   .remove_dupes()

    def get_publishers_names(self):
        '''get all publishers' names, no duplicates'''
        return self._database.books.select(lambda book: book.publisher) \
                                   .select(lambda publisher: publisher.name) \
                                   .remove_dupes()

    def get_books(self, *args, **kwargs):
        return self._database.books.where(*args, **kwargs)
