''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from typing  import List
from hashlib import sha256
from uuid    import uuid4

from . import key_property, BaseModel
from . import Book, Review


class User(BaseModel):

    def __init__(self, username: str, password: str):
        self.__username = username.strip().lower() \
            if isinstance(username, str) and username.strip() \
            else None
        self.__password = self.salt_hash(password) \
            if isinstance(password,  str) and len(password)>=7  \
            else None
        self.__read_books = []
        self.__reviews    = []
        self.__pages_read = 0

    def __repr__(self):
        return f'<User {self.username}>'

    #################   instance methods   #################

    def read_a_book(self, book: Book):
        if not isinstance(book, Book): return
        self.__read_books.append(book)
        self.__pages_read += book.num_pages if book.num_pages else 0

    def add_review(self, review: Review):
        if isinstance(review, Review):
            self.__reviews.append(review)

    ##################   static methods   ##################
    @staticmethod
    def salt_hash(password):
        '''salt-hash passwords for security'''
        salt = uuid4().hex
        salted_hash = sha256((salt+password).encode()).hexdigest()
        return f'{salted_hash}:{salt}'

    ####################   properties   ####################
    @key_property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def read_books(self) -> List[Book]:
        return self.__read_books

    @property
    def reviews(self) -> List[Review]:
        return self.__reviews

    @property
    def pages_read(self) -> int:
        return self.__pages_read
