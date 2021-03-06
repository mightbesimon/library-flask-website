''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from hashlib import sha256
from flask   import session

from .abstract_repository import AbstractRepository
from .memory_datacontext  import MemoryDataContext

class MemoryRepository(AbstractRepository):

    def __init__(self, database=MemoryDataContext()):
        self._database = database

    def username_exists(self, username):
        return self._database.users.any(username=username.lower())

    def add_user(self, user):
        '''returns a copy of the entry added to the database'''
        entry = self._database.users.add(user)
        self._database.save_changes()
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

    def get_users(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.users.where(*args, **kwargs)

    def get_current_user(self):
        return self.get_user(username=session['username']) \
            if 'username' in session else None

    def get_catalogue(self):
        '''get all books in the catalogue'''
        return self._database.catalogue

    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.books.first_or_default(**kwargs)

    def get_books(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.books.where(*args, **kwargs)

    def get_reviews(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.reviews.where(*args, **kwargs)

    def add_review(self, review):
        '''returns a copy of the entry added to the database'''
        entry = self._database.reviews.add(review)
        self._database.save_changes()
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

    def toggle_read(self, user, book):
        if book in user.books_read:
            user.books_read.remove(book)
        else:
            user.read_a_book(book)

    def toggle_follow(self, user, other):
        if other in user.following:
            user.unfollow(other)
        else:
            user.follow(other)
