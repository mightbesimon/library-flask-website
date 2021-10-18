''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE THREE
    Simon Shan  441147157
'''

from hashlib import sha256
from flask   import session

from . import DataSet
from .abstract_repository     import AbstractRepository
from .database_sessioncontext import DatabaseSessionContext
from ..models import Book, User, Review

class DatabaseRepository(AbstractRepository):

    def __init__(self, Session):
        self._context = DatabaseSessionContext(Session)

    def username_exists(self, username):
        return DataSet(self._context.session.query(User)).any(username=username.lower())

    def add_user(self, user):
        '''returns a copy of the entry added to the database'''
        with self._context as context:
            context.session.add(user)
            context.session.commit()

    def authenticate_user(self, username, password):
        user = DataSet(self._context.session.query(User)).first_or_default(username=username.lower())
        if not user: return False
        salted_hash, salt = user.password.split(':')
        # re-salt-hash the provided password and check if match
        return salted_hash == sha256((salt+password).encode()).hexdigest()

    def get_user(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return DataSet(self._context.session.query(User)).first_or_default(**kwargs)

    def get_users(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return DataSet(self._context.session.query(User)).where(*args, **kwargs)

    def get_current_user(self):
        return self.get_user(username=session['username']) \
            if 'username' in session else None

    def get_catalogue(self):
        '''get all books in the catalogue'''
        return DataSet(self._context.session.query(Book))

    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return DataSet(self._context.session.query(Book)).first_or_default(**kwargs)

    def get_books(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return DataSet(self._context.session.query(Book)).where(*args, **kwargs)

    def get_reviews(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return DataSet(self._context.session.query(Review)).where(*args, **kwargs)

    def add_review(self, review):
        '''returns a copy of the entry added to the database'''
        with self._context as context:
            context.session.add(review)
            context.session.commit()

    def get_authors_names(self):
        '''get all authors' names, no duplicates'''
        return DataSet(self._context.session.query(Book)) \
                    .select(lambda book: book.authors) \
                    .flatten() \
                    .select(lambda author: author.full_name) \
                    .remove_dupes()

    def get_release_years(self):
        '''get all release years, no duplicates'''
        return DataSet(self._context.session.query(Book)) \
                    .select(lambda book: book.release_year) \
                    .remove_dupes()

    def get_publishers_names(self):
        '''get all publishers' names, no duplicates'''
        return DataSet(self._context.session.query(Book)) \
                    .select(lambda book: book.publisher) \
                    .select(lambda publisher: publisher.name) \
                    .remove_dupes()
