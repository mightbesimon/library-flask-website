''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

class key_property(property):
    '''marks a property as the key'''
    def __set_name__(self, owner, name):
        owner.key = self

class BaseModel:
    '''uses the marked key property for comparisons and hashs'''

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
           and self.key==other.key

    def __lt__(self, other):
        return self.key < other.key

    def __hash__(self):
        return hash(self.key)


#======[!] * * *   help with imports   * * * [!]======#
from library.models.publisher import Publisher
from library.models.author    import Author
from library.models.book      import Book
from library.models.review    import Review
from library.models.user      import User
from library.models.inventory import BooksInventory
#======[!] * * *   help with imports   * * * [!]======#
