''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from library.adapters.IRepository import IRepository
from library.adapters.JsonDataContext import JsonDataContext

class LibraryRepository(IRepository):

    def __init__(self):
        self._database = JsonDataContext()

    def get_catalogue(self):
        return self._database.catalogue

    def get_all_books(self):
        '''an alias to get_catalogue'''
        return self._database.books

    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        return self._database.books.first_or_default(**kwargs)