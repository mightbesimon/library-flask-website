''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, session, render_template

from ..adapters import _repo
from ..handlers import nav, authorisation, useronly


blueprint = Blueprint('account', __name__)


@blueprint.route('/account')
@authorisation(useronly)
def account():
    user = _repo.get_user(username=session['username'])
    return render_template('account.html', nav=nav, user=user)
