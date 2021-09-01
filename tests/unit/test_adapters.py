''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

import pytest

from library.adapters.DataSet import DataSet
from library.adapters.LibraryDataContext import LibraryDataContext
from library.adapters.LibraryRepository  import LibraryRepository

class Container:
    '''for linq testing'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'x{self.x}y{self.y}'

class TestDataSet:

    def test_initialisation(self):
        assert repr(DataSet())=='[]'
        list1 = [1, 2, 3]
        assert repr(DataSet(list1))=='[1, 2, 3]'

    def test_linq_where(self):
        container1 = Container(11, 11)
        container2 = Container(11, 99)
        container3 = Container(99, 11)
        container_dataset = DataSet([container1, container2, container3])

        # test kwargs
        assert container1 in container_dataset.where(x=11)
        assert container2 in container_dataset.where(x=11)
        assert container3 not in container_dataset.where(x=11)

        # test no kwargs
        assert container1 in container_dataset.where()
        assert container2 in container_dataset.where()
        assert container3 in container_dataset.where()

    def test_linq_first_or_default(self):
        container1 = Container(11, 11)
        container2 = Container(11, 99)
        container3 = Container(99, 11)
        container_dataset = DataSet([container1, container2, container3])

        # test kwargs
        assert container3 is container_dataset.first_or_default(x=99)
        assert container3 is container_dataset.first_or_default(x=99, default=container1)
        assert None is container_dataset.first_or_default(x=0)

        # test defaults
        assert container1 is container_dataset.first_or_default(x=0, default=container1)
        assert container2 is container_dataset.first_or_default(default=container2, x=0)
        assert container3 is container_dataset.first_or_default(container3, x=0)

        # test no kwargs
        assert container1 is container_dataset.first_or_default(container3)

    def test_linq_select(self):
        container1 = Container(11, 11)
        container2 = Container(11, 99)
        container3 = Container(99, 11)
        container_dataset = DataSet([container1, container2, container3])

        x_dataset = container_dataset.select(lambda container: container.x)
        assert isinstance(x_dataset, DataSet)
        assert x_dataset==[11, 11, 99]


@pytest.fixture
def database():
    return LibraryDataContext()

class TestLibraryDataContext:

    def test_catalogue(self, database):
        assert isinstance(database.catalogue, DataSet)
        assert database.books==database.catalogue
        assert len(database.catalogue) > 0
        assert repr(database.catalogue.first_or_default())=='<Book The Switchblade Mamma, book id = 25742454>'

    def test_users(self, database):
        assert isinstance(database.users, DataSet)
        # TODO

    def test_reviews(self, database):
        assert isinstance(database.reviews, DataSet)
        # TODO


@pytest.fixture
def repo():
    return LibraryRepository()

class TestLibraryRepository:

    def test_initialisation(self, repo):
        assert isinstance(repo._database, LibraryDataContext)

    def test_get_catalogue(self, repo):
        catalogue = repo.get_catalogue()
        assert isinstance(catalogue, DataSet)
        assert repr(catalogue.first_or_default())=='<Book The Switchblade Mamma, book id = 25742454>'

    def test_get_all_books(self, repo):
        assert repo.get_all_books() is repo.get_catalogue()

    def test_get_book(self, repo):
        assert repr(repo.get_book())=='<Book The Switchblade Mamma, book id = 25742454>'
        assert repr(repo.get_book(book_id=27036539))=='<Book War Stories, Volume 4, book id = 27036539>'
        assert repr(repo.get_book(book_id=0))=='None'
        assert repr(repo.get_book(default=-1, book_id=0))=='-1'
