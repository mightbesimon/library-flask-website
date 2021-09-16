''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Flask

from config import EnvConfig
from .blueprints import catalogue, authentication


def create_app():
    app = Flask(__name__)
    app.config.from_object(EnvConfig)           # configure flask app
    
    app.register_blueprint(authentication.blueprint)
    app.register_blueprint(catalogue.blueprint) # register blueprints

    return app