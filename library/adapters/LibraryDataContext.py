''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from .jsondatareader import BooksJSONReader, UsersJSONReader
from .DataSet import DataSet

# path constants
DATA_DIRECTORY   = 'library/data/'
FILENAME_BOOKS   = DATA_DIRECTORY+'comic_books_excerpt.json'
FILENAME_AUTHORS = DATA_DIRECTORY+'book_authors_excerpt.json'
FILENAME_USERS   = DATA_DIRECTORY+'dummy_users_and_reviews.json'


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

        # read in users and reviews
        reader = UsersJSONReader(FILENAME_USERS)
        reader.read_json_file(self.catalogue)
        self._users   = DataSet(reader.dataset_of_users)
        self._reviews = DataSet(reader.dataset_of_reviews)
