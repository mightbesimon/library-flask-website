''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from datetime import datetime

from . import key_property, BaseModel
from . import Book


class Review(BaseModel):

    def __init__(self, book: Book, review_text: str, rating: int):
        self.__book = book if isinstance(book, Book) else None
        self.__review_text = review_text.strip() \
                    if isinstance(review_text, str) else 'N/A'
        if not 1<=rating<=5: raise ValueError
        self.__rating = rating
        self.__timestamp = datetime.now()

    def __repr__(self):
        return f'<Review of book {self.book}, rating = {self.rating}, timestamp = {self.timestamp}>'

    ####################   properties   ####################
    @property
    def book(self) -> Book:
        return self.__book

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @key_property
    def timestamp(self) -> datetime:
        return self.__timestamp
