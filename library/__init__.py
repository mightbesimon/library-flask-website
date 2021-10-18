''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO & THREE
    Simon Shan  441147157
'''

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import EnvConfig


def create_app(ConfigObj=EnvConfig):
    app = Flask(__name__)


    ##############   configure flask app   ###############

    app.config.from_object(ConfigObj)           # default = EnvConfig
                                                # testing = TestingConfig


    ############   instantiate a repository   ############

    from . import adapters
    from .adapters import MemoryRepository, DatabaseRepository, map_orm, migration

    if ConfigObj.REPOTYPE=='memory':
        adapters._repo = MemoryRepository()     # instantiate a memory repository


    if ConfigObj.REPOTYPE=='database':
        uri  = ConfigObj.SQLALCHEMY_DATABASE_URI
        echo = ConfigObj.SQLALCHEMY_ECHO        # configs

        engine = create_engine(uri, echo=echo, poolclass=NullPool,
                    connect_args={"check_same_thread": False})
                                                # this is just how SQLAlchemy works
        Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
                                                # global database session factory for making fresh sessions
        adapters._repo = DatabaseRepository(Session)
                                                # instantiate a database repository

        map_orm() if engine.table_names() else migration.add(engine)


    ##############   register blueprints   ###############

    from .blueprints import home, catalogue, authentication, account, error

    app.register_blueprint(error.blueprint)     # custom 404 error page

    app.register_blueprint(home.blueprint)
    app.register_blueprint(authentication.blueprint)
    app.register_blueprint(account.blueprint)
    app.register_blueprint(catalogue.blueprint)


    return app
