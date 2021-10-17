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
        self._username = username.strip().lower() \
            if isinstance(username, str) and username.strip() \
            else None
        self._password = self.salt_hash(password) \
            if isinstance(password,  str) and len(password)>=7  \
            else None
        self._books_read = []
        self._reviews    = []
        self._pages_read = 0
        self._followers  = []
        self._following  = []

    def __repr__(self):
        return f'<User {self.username}>'

    #################   instance methods   #################

    def read_a_book(self, book: Book):
        if not isinstance(book, Book): return
        self._books_read.append(book)
        self._pages_read += book.num_pages if book.num_pages else 0

    def add_review(self, review: Review):
        if isinstance(review, Review):
            self._reviews.append(review)


    def follow(self, user: 'User'):
        self.following.append(user)
        user.followers.append(self)

    def unfollow(self, user: 'User'):
        while user in self.following:
            self.following.remove(user)
        while self in user.followers:
            user.followers.remove(self)

    def num_books_read(self):
        return len(self.books_read)

    def num_reviews(self):
        return len(self.reviews)

    def num_followers(self):
        return len(self.followers)

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
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def books_read(self) -> List[Book]:
        return self._books_read

    @property
    def reviews(self) -> List[Review]:
        return self._reviews

    @property
    def pages_read(self) -> int:
        return self._pages_read

    @property
    def followers(self) -> int:
        return self._followers

    @property
    def following(self) -> int:
        return self._following
