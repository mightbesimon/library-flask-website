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
    _database.books.where(lambda book: book.id in [1,2,3])  # get books with id 1, 2 and 3
    _database.books.where(lambda book: book.release_year<2021 and book.ebook)
                                                            # get all books before 2021 and only ebooks
    _database.users.any(username='jamesbond')               # check if username jamesbond already exists
    _database.users.any(username='bond', password='007')    # authenticate user credentials
    _database.books.all(ebook=True)                         # check if all books are ebooks
    '''
    def add(self, entry):
        '''returns a copy of the entry added to the database'''
        self.append(entry)
        return entry

    def where(self, function=None, **kwargs):
        '''returns a DataSet to allow chaining queries'''
        
        # if no specified function, use kwargs for matches
        if not function:
            function = lambda item: all(getattr(item, attribute)==value for attribute, value in kwargs.items())

        # returns a DataSet to allow chaining queries
        return type(self)(item for item in self if function(item))


    def first_or_default(self, default=None, **kwargs):
        return next(iter(self.where(**kwargs)), default)

    def select(self, function=None):
        '''returns a DataSet to allow chaining queries'''
        return type(self)(map(function, self))

    def any(self, function=None, **kwargs):
        return any(self.where(function=function, **kwargs))

    def all(self, function=None, **kwargs):
        return len(self)==len(self.where(function=function, **kwargs))

    def order_by(self, key=None, reverse=False):
        return type(self)(sorted(self, key=key, reverse=reverse))

    def then_by(self, key=None):
        ...

    def flatten(self):
        '''flatten from 2D list to 1D list'''
        return type(self)(item for one_list in self for item in one_list)

    def remove_dupes(self):
        '''preserves order'''
        # `type(self)(set(self))` doesn't preserve order
        return type(self)(dict.fromkeys(self))

    def sort(self, *args, **kwargs):
        super().sort(*args, **kwargs)
        return self

    def remove(self, item):
        if item in self:
            super().remove(item)
        return self
