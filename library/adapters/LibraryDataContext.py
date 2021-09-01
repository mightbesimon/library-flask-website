''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from library.adapters.jsondatareader import BooksJSONReader
from library.adapters.DataSet import DataSet

# path constants
DATA_DIRECTORY   = 'library/data/'
FILENAME_BOOKS   = DATA_DIRECTORY+ 'comic_books_excerpt.json'
FILENAME_AUTHORS = DATA_DIRECTORY+'book_authors_excerpt.json'


class LibraryDataContext:

    @property
    def catalogue(self) -> DataSet:
        '''the catalogue of books of the library
           contains data from both book and author json files'''
        return self._catalogue

    @property
    def books(self) -> DataSet:
        '''an alias for catalogue
           the catalogue includes books but also authors'''
        return self._catalogue
    
    @property
    def users(self) -> DataSet:
        '''registered users of the library'''
        return self._users

    @property
    def reviews(self) -> DataSet:
        '''reviews left on this site'''
        return self._reviews

    def __init__(self):
        # read in the books
        reader = BooksJSONReader(FILENAME_BOOKS, FILENAME_AUTHORS)
        reader.read_json_files()

        self._catalogue = DataSet(reader.dataset_of_books)
        self._users     = DataSet()
        self._reviews   = DataSet()
