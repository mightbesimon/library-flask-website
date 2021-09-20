''' Copyright 2021 mightbesimon | github.com/mightbesimon
    All rights reserved.
'''

from flask import session, redirect


class Policy:
    '''authorisation policy
usage examples:
    useronly   = Policy('username', _repo.username_exists)  # only users may acess the content
    aged21over = Policy('age'     , _repo.old_enough     )  # only aged 21 or over may access
    '''
    def __init__(self, session_key, verification_function):
        self.session_key = session_key
        self.verification_function = verification_function

    def verify(self):
        return self.session_key in session \
           and self.verification_function(session[self.session_key])


class authorisation:
    '''authorisation decorator with args
usage examples:
    @authorisation(userOnly)                # only users may access the content
    @authorisation(useronly, aged21over)    # only users aged 21 and over may access
    '''
    def __init__(self, *policies):
        self.policies = policies

    def __call__(self, function):
        self.function = function
        return self.authorise
    
    def authorise(self, *args, **kwargs):
        if all(policy.verify() for policy in self.policies):
            return self.function(*args, **kwargs)
        else:
            return redirect('/login')
