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

        self.__book_id = book_id
        self.title     = book_title     #  use setter

        self.__description  = None
        self.__publisher    = None
        self.__authors      = []
        self.__release_year = None
        self.__ebook        = None
        self.__num_pages    = None
        self.__image_url    = None
        self.__similar_books= []
        self.__language     = None

    def __repr__(self):
        return f'<Book {self.title}, book id = {self.book_id}>'

    #################   instance methods   #################

    def add_author(self, author: Author):
        if isinstance(author, Author) and author not in self.authors:
            self.authors.append(author)

    def remove_author(self, author: Author):
        if isinstance(author, Author) and author in self.__authors:
            self.__authors.remove(author)

    def short_title(self, ch=56):
        return self.title[:ch]+'...' if len(self.title) > ch else self.title

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

    @property
    def image_url(self) -> str:
        return self.__image_url
    @image_url.setter
    def image_url(self, image_url: str):
        if not isinstance(image_url, str) or not image_url.strip():
            raise ValueError
        self.__image_url = image_url.strip()

    @property
    def similar_books(self) -> List['Book']:
        return self.__similar_books
    @similar_books.setter
    def similar_books(self, similar_books: List['Book']):
        self.__similar_books = similar_books
    
    @property
    def language(self) -> str:
        return self.__language
    @language.setter
    def language(self, language_code: str):
        self.__language = language_code
