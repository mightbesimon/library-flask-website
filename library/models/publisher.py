''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from . import key_property, BaseModel


class Publisher(BaseModel):

    def __init__(self, publisher_name: str):
        self.name = publisher_name      # use setter

    def __repr__(self):
        return f'<Publisher {self.name}>'

    ####################   properties   ####################
    @key_property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name: str):
        self.__name = publisher_name.strip() \
            if isinstance(publisher_name, str) and publisher_name.strip() \
            else 'N/A'
