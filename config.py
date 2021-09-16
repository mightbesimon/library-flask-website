''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
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

    # TESTING = environ.get('TESTING')
