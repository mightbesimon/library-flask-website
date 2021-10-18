''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE THREE
    Simon Shan  441147157
'''

from sqlalchemy.orm import clear_mappers

from . import metadata, map_orm, DataSet
from .jsondatareader import BooksJSONReader, UsersJSONReader

# path constants
DATA_DIRECTORY   = 'library/data/'
FILENAME_BOOKS   = DATA_DIRECTORY+'comic_books_excerpt.json'
FILENAME_AUTHORS = DATA_DIRECTORY+'book_authors_excerpt.json'
FILENAME_USERS   = DATA_DIRECTORY+'dummy_users_and_reviews.json'


def add(engine):
    print('\n\n[!] * * * Adding new migration... * * * [!]\n')
    
    clear_mappers()                     # reset the database mapping
    metadata.create_all(engine)         # generate all tables associated with the metadata
    
    for table in reversed(metadata.sorted_tables):
        engine.execute(table.delete())  # clean out the existing data from tables

    map_orm()
    from . import _repo
    populate(_repo._context)

    print('\n[!] * * * New migration succussfully added * * * [!]\n\n')


def populate(session_context):
    with session_context as context:
        reader = BooksJSONReader(FILENAME_BOOKS, FILENAME_AUTHORS)
        reader.read_json_files()
        for author in reader.dataset_of_authors:
            context.session.add(author)
        print('===== Authors Loaded =====')
        books = reader.dataset_of_books
        for book in books:
            context.session.add(book)
        print('=====  Books Loaded  =====')

        reader = UsersJSONReader(FILENAME_USERS)
        reader.read_json_file(DataSet(books))
        for user in reader.dataset_of_users:
            context.session.add(user)
        print('=====  Users Loaded  =====')
        for review in reader.dataset_of_reviews:
            context.session.add(review)
        print('===== Reviews Loaded =====')
        context.session.commit()
