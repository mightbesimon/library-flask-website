''' Copyright 2021 mightbesimon | github.com/mightbesimon
    All rights reserved.
'''

class DataSet(list):
    '''provide LINQ like methods for data storing lists
usage examples:
    _database.books.where(ebook=True, release_year=2020)    # get all ebooks released in 2020
                   .select(lambda e: (e.title, e.author))   # only get the titles and authors

    _database.author.first_or_default(full_name='Ronald J. Fields', EmptyAuthor())
                                                            # get the first author with the name Ronald J. Fields
                                                            # or return an EmptyAuthor()
    '''
    def where(self, **kwargs):
        '''returns a DataSet to allow chaining queries'''
        # helper
        is_match = lambda item: all(getattr(item, attribute)==value for attribute, value in kwargs.items())

        # returns a DataSet to allow chaining queries
        return type(self)(item for item in self if is_match(item))


    def first_or_default(self, default=None, **kwargs):
        items = self.where(**kwargs)
        return items[0] if len(items) else default


    def select(self, function=None):
        '''returns a DataSet to allow chaining queries'''
        return type(self)(function(item) for item in self)

    def order_by(self, function):
        ...

    def then_by(self, function):
        ...
