''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE THREE
    Simon Shan  441147157
'''

import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, clear_mappers

from library import adapters
from library.adapters import metadata, map_orm, migration, DatabaseRepository
from library.models   import User, Review

IN_MEMORY_DATABASE_URI = 'sqlite://'
FILE_DATABASE_URI = 'sqlite:///tests/testingDB.sqlite'


def engine_factory(databaseURI):
    clear_mappers()                         # reset the database mapping
    engine = create_engine(databaseURI)
    metadata.create_all(engine)             # generate all tables associated with the metadata
    for table in reversed(metadata.sorted_tables):
        engine.execute(table.delete())      # clean out the existing data from tables
    map_orm()
    return engine



@pytest.fixture
def session_populated():
    engine = engine_factory(FILE_DATABASE_URI)
    Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
                                                    # global database session factory for making fresh sessions
    adapters._repo = DatabaseRepository(Session)    # instantiate a database repository
    migration.add(engine)                           # populate
    yield Session
    metadata.drop_all(engine)

@pytest.fixture
def session_empty():
    engine = engine_factory(IN_MEMORY_DATABASE_URI)
    Session = sessionmaker(bind=engine)             # global database session factory for making fresh sessions
    yield Session()
    metadata.drop_all(engine)



class TestDatabaseORM:

    def test_saving_loading_users(self, session_empty):
        session_empty.add(User('Alan Turing', 'password'))
        session_empty.add(User('Simon', 'password'))
        session_empty.commit()

        assert [('alan turing',), ('simon',)]==list(session_empty.execute('SELECT username FROM Users'))

    def test_following_users(self, session_empty):
        turing = User('Alan Turing', 'password')
        simon  = User('Simon'      , 'password')
        session_empty.add(turing)
        session_empty.add(simon)
        turing.follow(simon)        # turing follows simon
        session_empty.commit()      # this change is saved in the database upon commit

        assert [(1,2)]==list(session_empty.execute('SELECT followerID, followingID FROM FollowersAssociation'))


class TestDatabaseRepository:

    def test_initialisation(self, session_populated):
        # assert isinstance(repo._database, MemoryDataContext)
        ...

    def test_get_catalogue(self, session_populated):
        # catalogue = repo.get_catalogue()
        # assert isinstance(catalogue, DataSet)
        # assert repr(catalogue.first_or_default())=='<Book The Switchblade Mamma, book id = 25742454>'
        ...

    def test_get_books(self, session_populated):
        # assert repo.get_books() == repo.get_catalogue()
        ...

    def test_get_book(self, session_populated):
        # assert repr(repo.get_book())=='<Book The Switchblade Mamma, book id = 25742454>'
        # assert repr(repo.get_book(book_id=27036539))=='<Book War Stories, Volume 4, book id = 27036539>'
        # assert repr(repo.get_book(book_id=0))=='None'
        # assert repr(repo.get_book(default=-1, book_id=0))=='-1'
        ...
