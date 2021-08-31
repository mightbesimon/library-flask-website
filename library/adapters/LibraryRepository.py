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

    def get_books(self):
        return self._database.books

    def get_book_by_id(self, id):
        book, *_ = [book for book in self._database.catalogue if book.book_id==int(id)]
        return book