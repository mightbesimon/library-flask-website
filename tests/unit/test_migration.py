''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE THREE
    Simon Shan  441147157
'''

import pytest
from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import sessionmaker, clear_mappers

from library import adapters
from library.adapters import metadata, map_orm, migration, DatabaseRepository


FILE_DATABASE_URI = 'sqlite:///tests/testingDB.sqlite'


@pytest.fixture
def engine_populated():
    clear_mappers()                                 # reset the database mapping
    engine = create_engine(FILE_DATABASE_URI)
    metadata.create_all(engine)                     # generate all tables associated with the metadata
    for table in reversed(metadata.sorted_tables):
        engine.execute(table.delete())              # clean out the existing data from tables
    map_orm()
    Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
                                                    # global database session factory for making fresh sessions
    adapters._repo = DatabaseRepository(Session)    # instantiate a database repository
    migration.add(engine)                           # populate
    yield engine
    metadata.drop_all(engine)



class TestMigration:

    def test_table_names(self, engine_populated):
        table_names = inspect(engine_populated).get_table_names()
        assert 'Publishers'            in table_names
        assert 'Authors'               in table_names
        assert 'Books'                 in table_names
        assert 'AuthorshipAssociation' in table_names
        assert 'Users'                 in table_names
        assert 'BooksReadAssociation'  in table_names
        assert 'Reviews'               in table_names
        assert 'FollowersAssociation'  in table_names

    def test_publishers_table(self, engine_populated):
        with engine_populated.connect() as connection:

            result = connection.execute(select([metadata.tables['Publishers']]))
            publisher_names = [row['name'] for row in result]

            assert 'Avatar Press' in publisher_names
            assert 'DC Comics' in publisher_names
            assert 'Marvel' in publisher_names
            assert 'N/A' in publisher_names

    def test_authors_table(self, engine_populated):
        with engine_populated.connect() as connection:

            result = connection.execute(select([metadata.tables['Authors']]))
            author_ids = [row['authorID'] for row in result]

            assert 163 in author_ids
            assert 796 in author_ids
            assert 865 in author_ids
            assert 870 in author_ids
            assert 892 in author_ids

    def test_books_table(self, engine_populated):
        with engine_populated.connect() as connection:

            result = connection.execute(select([metadata.tables['Books']]))
            book_languages = [row['language'] for row in result]

            assert 'French'   in book_languages
            assert 'Korean'   in book_languages
            assert 'Japanese' in book_languages
            assert 'Chinese'  in book_languages
            assert 'Spanish'  in book_languages
            assert 'English'  in book_languages
            assert 'English (American)' in book_languages

    def test_users_table(self, engine_populated):
        with engine_populated.connect() as connection:

            result = connection.execute(select([metadata.tables['Users']]))
            usernames = [row['username'] for row in result]

            assert 'mightbesimon'  in usernames
            assert 'alan turing'   in usernames
            assert 'julius-caesar' in usernames
            assert 'jamesbond'     in usernames

    def test_reviews_table(self, engine_populated):
        with engine_populated.connect() as connection:

            result = connection.execute(select([metadata.tables['Reviews']]))
            book_ids = [row['bookID'] for row in result]

            assert 25742454 in book_ids
            assert 13571772 in book_ids
            assert 30128855 in book_ids
