''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from . import key_property, BaseModel
from . import Book


class BooksInventory:

    def __init__(self):
        self._books = {}
        self._prices = {}
        self._stock_count = {}

    def add_book(self, book: Book, price: int, stock_count: int):
        self._books[book.book_id] = book
        self._prices[book.book_id] = price
        self._stock_count[book.book_id] = stock_count

    def remove_book(self, book_id: int):
        self._books.pop(book_id)
        self._prices.pop(book_id)
        self._stock_count.pop(book_id)

    def find_book(self, book_id: int):
        if book_id in self._books:
            return self._books[book_id]

    def find_price(self, book_id: int):
        if book_id in self._books:
            return self._prices[book_id]

    def find_stock_count(self, book_id: int):
        if book_id in self._books:
            return self._stock_count[book_id]

    def search_book_by_title(self, book_title: str):
        for book_id, book in self._books.items():
            if book.title == book_title:
                return book
