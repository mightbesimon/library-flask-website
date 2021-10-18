''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def username_exists(self, username):
        raise NotImplementedError

    @abstractmethod
    def add_user(self, user):
        '''returns a copy of the entry added to the database'''
        raise NotImplementedError

    @abstractmethod
    def authenticate_user(self, username, password):
        raise NotImplementedError

    @abstractmethod
    def get_user(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        raise NotImplementedError

    @abstractmethod
    def get_users(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        raise NotImplementedError

    @abstractmethod
    def get_current_user(self):
        raise NotImplementedError

    @abstractmethod
    def get_catalogue(self):
        '''get all books in the catalogue'''
        raise NotImplementedError

    @abstractmethod
    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        raise NotImplementedError

    @abstractmethod
    def get_books(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        raise NotImplementedError

    @abstractmethod
    def get_reviews(self, *args, **kwargs):
        '''uses LINQ support in DataSet class'''
        raise NotImplementedError

    @abstractmethod
    def add_review(self, review):
        '''returns a copy of the entry added to the database'''
        raise NotImplementedError

    @abstractmethod
    def get_authors_names(self):
        '''get all authors' names, no duplicates'''
        raise NotImplementedError

    @abstractmethod
    def get_release_years(self):
        '''get all release years, no duplicates'''
        raise NotImplementedError

    @abstractmethod
    def get_publishers_names(self):
        '''get all publishers' names, no duplicates'''
        raise NotImplementedError
