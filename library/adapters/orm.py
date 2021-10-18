''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE THREE
    Simon Shan  441147157
'''

from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import mapper, relationship

from .. import models as model


# global variable giving access to the MetaData (schema) information of the database
metadata = MetaData()

class DbTablesContainer:
    '''database tables container for organisation'''

    Publishers = Table('Publishers', metadata,
        Column('publisherID', Integer, primary_key=True),
        Column('name', String(255), nullable=False),
    )

    Authors = Table('Authors', metadata,
        Column('authorID', Integer,  primary_key=True ),
        Column('fullname', String(255), nullable=False),
    )

    Books = Table('Books', metadata,
        Column('bookID'     , Integer,   primary_key=True         ),
        Column('title'      , String(255) , nullable=False        ),
        Column('description', String(1024), nullable=False        ),
        Column('publisherID', ForeignKey('Publishers.publisherID')),
        Column('releaseYear', Integer     ,                       ),
        Column('ebook'      , Boolean     ,                       ),
        Column('numPages'   , Integer     ,                       ),
        Column('imageURL'   , String(255) , nullable=False        ),
        Column('language'   , String(255) ,                       ),
    )

    AuthorshipAssociation = Table('AuthorshipAssociation', metadata,
        Column('authorID', ForeignKey('Books.bookID'    ), primary_key=True ),
        Column('bookID'  , ForeignKey('Authors.authorID'), primary_key=True ),
    )

    Users = Table('Users', metadata,
        Column('userID'   , Integer, primary_key=True, autoincrement=True),
        Column('username' , String(255), nullable=False, unique=True),
        Column('password' , String(255), nullable=False             ),
        Column('pagesRead', Integer    , nullable=False             ),
    )

    BooksReadAssociation = Table('BooksReadAssociation', metadata,
        Column('bookID', ForeignKey('Books.bookID'), primary_key=True ),
        Column('userID', ForeignKey('Users.userID'), primary_key=True ),
    )

    Reviews = Table('Reviews', metadata,
        Column('reviewID'  , Integer, primary_key=True, autoincrement=True),
        Column('bookID'    , ForeignKey('Books.bookID')  ),
        Column('userID'    , ForeignKey('Users.userID')  ),
        Column('reviewText', String(1024),               ),
        Column('rating'    , Integer     , nullable=False),
        Column('timestamp' , DateTime    , nullable=False),
    )

    FollowersAssociation = Table('FollowersAssociation', metadata,
        Column('followerID' , ForeignKey('Users.userID'), primary_key=True ),
        Column('followingID', ForeignKey('Users.userID'), primary_key=True ),
    )



table = DbTablesContainer()     # code organisation

def map_orm():
    mapper(model.Publisher, table.Publishers, properties={
        '_name': table.Publishers.c.name,
    })

    mapper(model.Author, table.Authors, properties={
        '_unique_id': table.Authors.c.authorID,
        '_full_name': table.Authors.c.fullname,
    })

    mapper(model.Book, table.Books, properties={
        '_book_id'     : table.Books.c.bookID,
        '_title'       : table.Books.c.title,
        '_description' : table.Books.c.description,
        '_publisher'   : relationship(model.Publisher),
        '_authors'     : relationship(model.Author, secondary=table.AuthorshipAssociation),
        '_release_year': table.Books.c.releaseYear,
        '_ebook'       : table.Books.c.ebook,
        '_num_pages'   : table.Books.c.numPages,
        '_image_url'   : table.Books.c.imageURL,
        '_language'    : table.Books.c.language,
    })

    mapper(model.User, table.Users, properties={
        '_username'  : table.Users.c.username,
        '_password'  : table.Users.c.password,
        '_books_read': relationship(model.Book  , secondary=table.BooksReadAssociation),
        '_reviews'   : relationship(model.Review),
        '_pages_read': table.Users.c.pagesRead,
        '_followers' : relationship(model.User  , secondary=table.FollowersAssociation,
                                        foreign_keys=table.FollowersAssociation.c.followerID ),
        '_following' : relationship(model.User  , secondary=table.FollowersAssociation,
                                        foreign_keys=table.FollowersAssociation.c.followingID),
    })

    mapper(model.Review, table.Reviews, properties={
        '_book'       : relationship(model.Book),
        '_user'       : relationship(model.User),
        '_review_text': table.Reviews.c.reviewText,
        '_rating'     : table.Reviews.c.rating,
        '_timestamp'  : table.Reviews.c.timestamp,
    })
