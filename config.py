''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO & THREE
    Simon Shan  441147157

    Flask configuration variables.
'''

from os import environ
from dotenv import load_dotenv

# Load environment variables from the .env stored in the project root.
load_dotenv()


class EnvConfig:
    '''configure Flask from environment variables'''

    FLASK_APP  = environ.get('FLASK_APP')
    FLASK_ENV  = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_ECHO = environ.get('SQLALCHEMY_ECHO')=='True'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    REPOTYPE = environ.get('REPOTYPE')


class TestingConfig(EnvConfig):
    '''override configuration for testing'''

    TESTING = True
    WTF_CSRF_ENABLED = False
    REPOTYPE = 'memory'
