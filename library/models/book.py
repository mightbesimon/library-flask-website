''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from typing import List

from . import key_property, BaseModel
from . import Publisher, Author


class Book(BaseModel):

    def __init__(self, book_id: int, book_title: str):
        if not isinstance(book_id, int) or book_id<0:
            raise ValueError

        self._book_id = book_id
        self.title    = book_title      #  use setter

        self._description  = None
        self._publisher    = None
        self._authors      = []
        self._release_year = None
        self._ebook        = None
        self._num_pages    = None
        self._image_url    = None
        self._similar_books= []
        self._language     = None

    def __repr__(self):
        return f'<Book {self.title}, book id = {self.book_id}>'

    #################   instance methods   #################

    def add_author(self, author: Author):
        if isinstance(author, Author) and author not in self.authors:
            self.authors.append(author)

    def remove_author(self, author: Author):
        if isinstance(author, Author) and author in self._authors:
            self._authors.remove(author)

    def short_title(self, ch=56):
        return self.title[:ch]+'...' if len(self.title) > ch else self.title

    ####################   properties   ####################
    @key_property
    def book_id(self) -> int:
        return self._book_id

    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, book_title: str):
        if not isinstance(book_title, str) or not book_title.strip():
            raise ValueError
        self._title = book_title.strip()

    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, description: str):
        if isinstance(description, str):
            self._description = description.strip()

    @property
    def publisher(self) -> Publisher:
        return self._publisher
    @publisher.setter
    def publisher(self, publisher: Publisher):
        if isinstance(publisher, Publisher):
            self._publisher = publisher

    @property
    def authors(self) -> List[Author]:
        return self._authors

    @property
    def release_year(self) -> int:
        return self._release_year
    @release_year.setter
    def release_year(self, release_year: int):
        if not isinstance(release_year, int) or release_year<0:
            raise ValueError
        self._release_year = release_year

    @property
    def ebook(self) -> bool:
        return self._ebook
    @ebook.setter
    def ebook(self, is_ebook: bool):
        if isinstance(is_ebook, bool):
            self._ebook = is_ebook

    @property
    def num_pages(self) -> int:
        return self._num_pages
    @num_pages.setter
    def num_pages(self, num_pages: int):
        if isinstance(num_pages, int) and num_pages >= 0:
            self._num_pages = num_pages

    @property
    def image_url(self) -> str:
        return self._image_url
    @image_url.setter
    def image_url(self, image_url: str):
        if not isinstance(image_url, str) or not image_url.strip():
            raise ValueError
        self._image_url = image_url.strip()

    @property
    def similar_books(self) -> List['Book']:
        return self._similar_books
    @similar_books.setter
    def similar_books(self, similar_books: List['Book']):
        self._similar_books = similar_books
    
    @property
    def language(self) -> str:
        return self._language
    @language.setter
    def language(self, language_code: str):
        self._language = language_code
