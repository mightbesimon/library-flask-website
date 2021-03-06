''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from datetime import datetime

from . import key_property, BaseModel
from . import Book


class Review(BaseModel):

    def __init__(self, book: Book, user: 'User', review_text: str, rating: int):
        self._book = book if isinstance(book, Book) else None
        self._user = user
        self._review_text = review_text.strip() \
                    if isinstance(review_text, str) else 'N/A'
        if not 1<=rating<=5: raise ValueError
        self._rating = rating
        self._timestamp = datetime.now()

    def __repr__(self):
        return f'<Review of book {self.book}, rating = {self.rating}, timestamp = {self.timestamp}>'

    ####################   properties   ####################
    @property
    def book(self) -> Book:
        return self._book

    @property
    def user(self) -> 'User':
        return self._user

    @property
    def review_text(self) -> str:
        return self._review_text

    @property
    def rating(self) -> int:
        return self._rating

    @key_property
    def timestamp(self) -> datetime:
        return self._timestamp
