''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from .IRepository import IRepository
from .LibraryDataContext import LibraryDataContext

class LibraryRepository(IRepository):

    def __init__(self):
        self._database = LibraryDataContext()

    def username_exists(self, username):
        return self._database.users.any(username=username)

    def add_user(self, user):
        '''returns a copy of the entry added to the database'''
        entry = self._database.users.add(user)
        return entry

    def authenticate_user(self, username, password):
        return self._database.users.any(username=username, password=password)

    def get_catalogue(self):
        return self._database.catalogue

    def get_all_books(self):
        '''an alias to get_catalogue'''
        return self._database.books

    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.books.first_or_default(**kwargs)