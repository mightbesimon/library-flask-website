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


class JsonDataContext:

    @property
    def catalogue(self) -> DataSet:
        '''the catalogue of books of the library'''
        return DataSet(self._catalogue)

    @property
    def books(self) -> DataSet:
        '''an alias for catalogue'''
        return DataSet(self._catalogue)
    
    @property
    def users(self) -> DataSet:
        return DataSet(self._users)

    @property
    def authors(self) -> DataSet:
        return DataSet(self._authors)

    @property
    def reviews(self) -> DataSet:
        return DataSet(self._reviews)
    
    @property
    def publishers(self) -> DataSet:
        return DataSet(self._publishers)

    def __init__(self):
        '''read in the books'''
        reader = BooksJSONReader(FILENAME_BOOKS, FILENAME_AUTHORS)
        reader.read_json_files()
        self._catalogue = reader.dataset_of_books
