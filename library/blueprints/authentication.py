''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, session

from ..adapters import _repo
from ..handlers import nav
from ..models   import User
from ..handlers import RegistrationForm, LoginForm


blueprint = Blueprint('authentication', __name__)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if not form.validate_on_submit():
        return render_template('credentials.html', nav=nav, form=form)

    _repo.add_user(User(form.username.data, form.password.data))
    session.clear()
    session['username'] = form.username.data.lower()
    return redirect('/account')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template('credentials.html', nav=nav, form=form)

    session.clear()
    session['username'] = form.username.data.lower()
    return redirect('/account')

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect('/')
