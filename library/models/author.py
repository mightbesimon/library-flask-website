''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from . import key_property, BaseModel


class Author(BaseModel):

    def __init__(self, author_id: int, author_full_name: str):
        if not isinstance(author_id, int) or author_id<0:
            raise ValueError
        self._unique_id = author_id
        self._coauthors = set()
        self.full_name  = author_full_name     # use setter

    def __repr__(self):
        return f'<Author {self.full_name}, author id = {self.unique_id}>'\

    #################   instance methods   #################

    def add_coauthor(self, coauthor):
        if self!=coauthor:
            self._coauthors.add(coauthor)
            # coauthor._coauthors.add(self)     # the tests didn't like that

    def check_if_this_author_coauthored_with(self, author):
        return author in self._coauthors

    ####################   properties   ####################
    @key_property
    def unique_id(self) -> int:
        return self._unique_id

    @property
    def full_name(self) -> str:
        return self._full_name
    @full_name.setter
    def full_name(self, author_full_name: str):
        if not isinstance(author_full_name, str) or not author_full_name.strip():
            raise ValueError
        self._full_name = author_full_name.strip()
