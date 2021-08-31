''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from abc import ABC, abstractmethod


class IRepository(ABC):

    @abstractmethod
    def get_catalogue(self):
        raise NotImplementedError

    @abstractmethod
    def get_books(self):
        raise NotImplementedError