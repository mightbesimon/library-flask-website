''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from library.adapters.jsondatareader import BooksJSONReader

# path constants
DATA_DIRECTORY   = 'library/data/'
FILENAME_BOOKS   = DATA_DIRECTORY+ 'comic_books_excerpt.json'
FILENAME_AUTHORS = DATA_DIRECTORY+'book_authors_excerpt.json'


class JsonDataContext:

    @property
    def catalogue(self):
        '''the catalogue of books of the library'''
        return self._catalogue

    @property
    def books(self):
        '''an alias for catalogue'''
        return self._catalogue
    
    @property
    def users(self):
        return self._users

    @property
    def authors(self):
        return self._authors

    @property
    def reviews(self):
        return self._reviews
    
    @property
    def publishers(self):
        return self._publishers

    def __init__(self):
        '''read in the books'''
        reader = BooksJSONReader(FILENAME_BOOKS, FILENAME_AUTHORS)
        reader.read_json_files()
        self._catalogue = reader.dataset_of_books
