''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE THREE
    Simon Shan  441147157
'''

from flask import _app_ctx_stack
from sqlalchemy.orm import scoped_session


class DatabaseSessionContext:

    def __init__(self, Session):
        self.Session = Session
        self.create_session()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._session.rollback()

    #################   instance methods   #################

    def create_session(self):
        self._session = scoped_session(self.Session,
                        scopefunc=_app_ctx_stack.__ident_func__)

    def close_session(self):
        if self._session: self._session.close()

    def reset_session(self):
        self.close_session()
        self.create_session()

    ####################   properties   ####################
    @property
    def session(self):
        return self._session
