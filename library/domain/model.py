''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from datetime import datetime
from typing import List


class key_property(property):
    '''marks a property as the key'''
    def __set_name__(self, owner, name):
        owner.key = self

class BaseModel:
    '''uses the property marked as the key for comparisons and hashs'''
    def __eq__(self, other):
        return isinstance(other, self.__class__) \
           and self.key==other.key

    def __lt__(self, other):
        return self.key < other.key

    def __hash__(self):
        return hash(self.key)

################################################################
####                       Publisher                        ####
################################################################
class Publisher(BaseModel):

    def __init__(self, publisher_name: str):
        self.name = publisher_name      # use setter

    def __repr__(self):
        return f'<Publisher {self.name}>'

    ####################   properties   ####################
    @key_property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name: str):
        self.__name = publisher_name.strip() \
            if isinstance(publisher_name, str) and publisher_name.strip() \
            else 'N/A'

################################################################
####                        Author                          ####
################################################################
class Author(BaseModel):

    def __init__(self, author_id: int, author_full_name: str):
        if not isinstance(author_id, int) or author_id<0:
            raise ValueError
        self.__unique_id = author_id
        self.__coauthors = set()
        self.full_name   = author_full_name     # use setter

    def __repr__(self):
        return f'<Author {self.full_name}, author id = {self.unique_id}>'\

    #################   instance methods   #################

    def add_coauthor(self, coauthor):
        if self!=coauthor:
            self.__coauthors.add(coauthor)
            # coauthor.__coauthors.add(self)    # the tests didn't like that

    def check_if_this_author_coauthored_with(self, author):
        return author in self.__coauthors

    ####################   properties   ####################
    @key_property
    def unique_id(self) -> int:
        return self.__unique_id

    @property
    def full_name(self) -> str:
        return self.__full_name
    @full_name.setter
    def full_name(self, author_full_name: str):
        if not isinstance(author_full_name, str) or not author_full_name.strip():
            raise ValueError
        self.__full_name = author_full_name.strip()

################################################################
####                         Book                           ####
################################################################
class Book(BaseModel):

    def __init__(self, book_id: int, book_title: str):
        if not isinstance(book_id, int) or book_id<0:
            raise ValueError

        self.__book_id = book_id
        self.title     = book_title     #  use setter

        self.__description = None
        self.__publisher   = None
        self.__authors     = []
        self.__release_year= None
        self.__ebook       = None
        self.__num_pages   = None

    def __repr__(self):
        return f'<Book {self.title}, book id = {self.book_id}>'

    #################   instance methods   #################

    def add_author(self, author: Author):
        if isinstance(author, Author) and author not in self.authors:
            self.authors.append(author)

    def remove_author(self, author: Author):
        if isinstance(author, Author) and author in self.__authors:
            self.__authors.remove(author)

    ####################   properties   ####################
    @key_property
    def book_id(self) -> int:
        return self.__book_id

    @property
    def title(self) -> str:
        return self.__title
    @title.setter
    def title(self, book_title: str):
        if not isinstance(book_title, str) or not book_title.strip():
            raise ValueError
        self.__title = book_title.strip()

    @property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, description: str):
        if isinstance(description, str):
            self.__description = description.strip()

    @property
    def publisher(self) -> Publisher:
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher: Publisher):
        if isinstance(publisher, Publisher):
            self.__publisher = publisher

    @property
    def authors(self) -> List[Author]:
        return self.__authors

    @property
    def release_year(self) -> int:
        return self.__release_year
    @release_year.setter
    def release_year(self, release_year: int):
        if not isinstance(release_year, int) or release_year<0:
            raise ValueError
        self.__release_year = release_year

    @property
    def ebook(self) -> bool:
        return self.__ebook
    @ebook.setter
    def ebook(self, is_ebook: bool):
        if isinstance(is_ebook, bool):
            self.__ebook = is_ebook

    @property
    def num_pages(self) -> int:
        return self.__num_pages
    @num_pages.setter
    def num_pages(self, num_pages: int):
        if isinstance(num_pages, int) and num_pages >= 0:
            self.__num_pages = num_pages

################################################################
####                        Review                          ####
################################################################
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

################################################################
####                         User                           ####
################################################################
class User(BaseModel):

    def __init__(self, username: str, password: str):
        self.__username  = username.strip().lower() \
            if isinstance(username, str) and username.strip() \
            else None
        self.__password   = password \
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

################################################################
####                    BooksInventory                      ####
################################################################
class BooksInventory:

    def __init__(self):
        self.__books = {}
        self.__prices = {}
        self.__stock_count = {}

    def add_book(self, book: Book, price: int, stock_count: int):
        self.__books[book.book_id] = book
        self.__prices[book.book_id] = price
        self.__stock_count[book.book_id] = stock_count

    def remove_book(self, book_id: int):
        self.__books.pop(book_id)
        self.__prices.pop(book_id)
        self.__stock_count.pop(book_id)

    def find_book(self, book_id: int):
        if book_id in self.__books:
            return self.__books[book_id]

    def find_price(self, book_id: int):
        if book_id in self.__books:
            return self.__prices[book_id]

    def find_stock_count(self, book_id: int):
        if book_id in self.__books:
            return self.__stock_count[book_id]

    def search_book_by_title(self, book_title: str):
        for book_id, book in self.__books.items():
            if book.title == book_title:
                return book
