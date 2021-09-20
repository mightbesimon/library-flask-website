''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from abc import ABC, abstractmethod


class IRepository(ABC):

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
    def get_catalogue(self):
        raise NotImplementedError

    @abstractmethod
    def get_all_books(self):
        '''an alias to get_catalogue'''
        raise NotImplementedError

    @abstractmethod
    def get_book(self, **kwargs):
        '''uses LINQ support in DataSet class'''
        raise NotImplementedError