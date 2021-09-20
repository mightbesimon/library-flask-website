''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, session, render_template

from ..adapters import _repo
from ..handlers import nav


blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def home():
    return render_template('home.html')

@blueprint.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', nav=nav)
