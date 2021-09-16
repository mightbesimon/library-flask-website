''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, session

from ..adapters import _repo
from ..models   import User
from ..handlers import RegistrationForm


blueprint = Blueprint('authentication', __name__)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if not form.validate_on_submit():
        return render_template('register.html', form=form)

    _repo.add_user(User(form.username.data, form.password.data))
    session.clear()
    session['username'] = form.username.data
    return redirect('/')
