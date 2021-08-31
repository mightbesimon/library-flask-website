''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from library.models import key_property, BaseModel


class Author(BaseModel):

    def __init__(self, author_id: int, author_full_name: str):
        if not isinstance(author_id, int) or author_id<0:
            raise ValueError
        self.__unique_id = author_id
        self.__coauthors = set()
        self.full_name   = author_full_name     # use setter

    def __repr__(self):
        return f'<Author {self.full_name}, author id = {self.unique_id}>'\

    #################   instance methods   #################

    def add_coauthor(self, coauthor):
        if self!=coauthor:
            self.__coauthors.add(coauthor)
            # coauthor.__coauthors.add(self)    # the tests didn't like that

    def check_if_this_author_coauthored_with(self, author):
        return author in self.__coauthors

    ####################   properties   ####################
    @key_property
    def unique_id(self) -> int:
        return self.__unique_id

    @property
    def full_name(self) -> str:
        return self.__full_name
    @full_name.setter
    def full_name(self, author_full_name: str):
        if not isinstance(author_full_name, str) or not author_full_name.strip():
            raise ValueError
        self.__full_name = author_full_name.strip()
