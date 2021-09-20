''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Flask

from config import EnvConfig
from .blueprints import home, catalogue, authentication, account


def create_app():
    app = Flask(__name__)
    app.config.from_object(EnvConfig)           # configure flask app
    
    app.register_blueprint(home.blueprint)      # register blueprints
    app.register_blueprint(authentication.blueprint)
    app.register_blueprint(account.blueprint)
    app.register_blueprint(catalogue.blueprint)

    return app