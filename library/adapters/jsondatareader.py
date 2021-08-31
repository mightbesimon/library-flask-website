''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

import json
from typing import List

from library.models import Publisher, Author, Book


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self) -> List[Book]:
        return self.__dataset_of_books

    def read_json_files(self):
        authors = {}

        # build the authors dictionary
        with open(self.__authors_file_name, 'r') as file:
            for line in file.read().split('\n'):
                if not line: continue
                author_data = json.loads(line)

                author_id   = int(author_data['author_id'])                 # author ID
                authors[author_id] = Author(author_id, author_data['name']) # auther full name

        # build the dataset of books
        with open(self.__books_file_name, 'r') as file:
            for line in file.read().split('\n'):
                if not line: continue
                book_data = json.loads(line)
                book = Book(int(book_data['book_id']), book_data['title'])  # book ID
                                                                            # book title
                book.publisher    = Publisher(book_data['publisher'])       # publisher
                book.description  = book_data['description']                # description

                if book_data['publication_year']:                           # release year
                    book.release_year = int(book_data['publication_year'])
                if book_data['is_ebook'].lower()=='true':                   # is ebook
                    book.ebook = True
                if book_data['is_ebook'].lower()=='false':                  # is not ebook
                    book.ebook = False
                if book_data['num_pages']:                                  # num pages
                    book.num_pages = int(book_data['num_pages'])

                # map authors to the book
                for author in book_data['authors']:                         # book authors
                    author_id = int(author['author_id'])
                    book.add_author(authors[author_id])

                self.dataset_of_books.append(book)
