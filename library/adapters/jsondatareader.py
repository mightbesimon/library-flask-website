''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

import json
from typing import List

from ..models import Publisher, Author, Book


class BooksJSONReader:

    def __init__(self, filename_books: str, filename_authors: str):
        self.__filename_books   = filename_books
        self.__filename_authors = filename_authors
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self) -> List[Book]:
        return self.__dataset_of_books

    def read_json_files(self):
        authors = {}            # authors from the author file
        books   = {}            # books   from the book   file
        books_authors = {}      # authors       of books mapping
        books_similar = {}      # similar_books of books mapping

        # build the authors dictionary
        with open(self.__filename_authors, 'r') as file:
            for line in file.read().split('\n'):
                if not line: continue
                author_data = json.loads(line)

                author_id   = int(author_data['author_id'])                 # author ID
                authors[author_id] = Author(author_id, author_data['name']) # auther full name

        # build the books dictionary
        # build the books_authors dictionary
        # build the books_similar dictionary
        with open(self.__filename_books, 'r') as file:
            for line in file.read().split('\n'):
                if not line: continue
                book_data = json.loads(line)
                book_id   = int(book_data['book_id'])                       # book ID
                book = Book(book_id, book_data['title'])                    # book title

                book.publisher    = Publisher(book_data['publisher'])       # publisher
                book.description  = book_data['description']                # description
                book.image_url    = book_data['image_url']                  # image_url

                if book_data['publication_year']:                           # release year
                    book.release_year = int(book_data['publication_year'])
                if book_data['is_ebook'].lower()=='true':                   # is ebook
                    book.ebook = True
                if book_data['is_ebook'].lower()=='false':                  # is not ebook
                    book.ebook = False
                if book_data['num_pages']:                                  # num pages
                    book.num_pages = int(book_data['num_pages'])

                books_authors[book_id] = book_data['authors']               # book authors
                books_similar[book_id] = book_data['similar_books']         # similar books

                books[book_id] = book

        # maps authors and similar books to book
        for book_id, book in books.items():

            # map authors to the book
            for author in books_authors[book_id]:
                author_id = int(author['author_id'])
                book.add_author(authors[author_id])

            # map similar books to the book
            for similar in books_similar[book_id]:
                book.similar_books = [books[int(_id)] for _id in similar 
                                                    if int(_id) in books]

        self.__dataset_of_books = list(books.values())
