''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

import pytest

from library.adapters import DataSet, MemoryDataContext, MemoryRepository


class Container:
    '''for linq testing'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'x{self.x}y{self.y}'

@pytest.fixture
def container1():
    return Container(11, 11)
@pytest.fixture
def container2():
    return Container(11, 99)
@pytest.fixture
def container3():
    return Container(99, 11)
@pytest.fixture
def container_dataset(container1, container2, container3):
    return DataSet([container1, container2, container3])

class TestDataSet:

    def test_initialisation(self):
        assert repr(DataSet())=='[]'
        list1 = [1, 2, 3]
        assert repr(DataSet(list1))=='[1, 2, 3]'

    def test_linq_where(self, container1, container2, container3, container_dataset):
        # test return type dataset
        assert isinstance(container_dataset.where(x=11), DataSet)

        # test kwargs
        assert container1 in container_dataset.where(x=11)
        assert container2 in container_dataset.where(x=11)
        assert container3 not in container_dataset.where(x=11)

        # test no kwargs
        assert container1 in container_dataset.where()
        assert container2 in container_dataset.where()
        assert container3 in container_dataset.where()

        # test function
        assert container1 in container_dataset.where(function=lambda c: c.x in [11, 99])
        assert container3 in container_dataset.where(lambda c: c.x in [11, 99])
        assert container3 not in container_dataset.where(lambda c: c.x in [11])

    def test_linq_first_or_default(self, container1, container2, container3, container_dataset):
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

    def test_linq_select(self, container1, container2, container3, container_dataset):
        x_dataset = container_dataset.select(lambda container: container.x)
        assert isinstance(x_dataset, DataSet)
        assert x_dataset==[11, 11, 99]

    def test_linq_any(self, container1, container2, container3, container_dataset):
        assert True ==container_dataset.any(x=11)
        assert False==container_dataset.any(x=19)
        assert True ==container_dataset.any(x=11, y=99)
        assert True ==container_dataset.any(lambda container: container.x+container.y==110)
        assert False==container_dataset.any(lambda container: container.x+container.y==100)

    def test_linq_all(self, container1, container2, container3, container_dataset):
        assert False==container_dataset.all(x=11)
        container_dataset.pop()
        assert True==container_dataset.all(x=11)


@pytest.fixture
def database():
    return MemoryDataContext()

class TestMemoryDataContext:

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
    return MemoryRepository()

class TestMemoryRepository:

    def test_initialisation(self, repo):
        assert isinstance(repo._database, MemoryDataContext)

    def test_get_catalogue(self, repo):
        catalogue = repo.get_catalogue()
        assert isinstance(catalogue, DataSet)
        assert repr(catalogue.first_or_default())=='<Book The Switchblade Mamma, book id = 25742454>'

    def test_get_books(self, repo):
        assert repo.get_books() == repo.get_catalogue()

    def test_get_book(self, repo):
        assert repr(repo.get_book())=='<Book The Switchblade Mamma, book id = 25742454>'
        assert repr(repo.get_book(book_id=27036539))=='<Book War Stories, Volume 4, book id = 27036539>'
        assert repr(repo.get_book(book_id=0))=='None'
        assert repr(repo.get_book(default=-1, book_id=0))=='-1'
