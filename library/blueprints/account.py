''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import Blueprint, render_template, redirect, session, request

from ..adapters import _repo
from ..handlers import nav, authorisation, useronly


blueprint = Blueprint('account', __name__)


@blueprint.route('/account')
@authorisation(policy=useronly)
def account():
    user = _repo.get_user(username=session['username'])
    discover = _repo.get_users() \
                .remove(user) \
                .where(lambda other: other not in user.following) \
                .order_by(lambda other: other.num_followers(), reverse=True)

    return render_template('account.html', nav=nav, user=user, discover=discover)

@blueprint.route('/account/follow')
@authorisation(policy=useronly)
def follow():
    user  = _repo.get_user(username=session['username'])
    other = _repo.get_user(username=request.args.get('username'))
    if other:
        if other in user.following:
            user.unfollow(other)
        else:
            user.follow(other)
    return redirect('/account#following')

@blueprint.route('/social')
@authorisation(policy=useronly)
def social():
    user = _repo.get_user(username=session['username'])
    discover = _repo.get_users() \
                .remove(user) \
                .where(lambda other: other not in user.following) \
                .order_by(lambda other: other.num_followers(), reverse=True)
    return render_template('social.html', nav=nav, user=user, discover=discover)

@blueprint.route('/social/follow')
@authorisation(policy=useronly)
def follow_social():
    user  = _repo.get_user(username=session['username'])
    other = _repo.get_user(username=request.args.get('username'))
    if other:
        if other in user.following:
            user.unfollow(other)
        else:
            user.follow(other)
    return redirect('/social#following')

# TODO: your suggestions
