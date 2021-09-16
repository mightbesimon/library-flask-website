''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Flask

from config import EnvConfig
from .blueprints import catalogue


def create_app():
    app = Flask(__name__)
    app.config.from_object(EnvConfig)       # configure flask app

    with app.app_context():                 # register blueprints
        app.register_blueprint(catalogue.blueprint)

    return app