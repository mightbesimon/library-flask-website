''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template

from ..handlers import nav


blueprint = Blueprint('error', __name__)


@blueprint.app_errorhandler(404)
def notfound(e):
	'''custom page for 404'''
	return render_template('notfound.html', nav=nav), 404
