''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

from flask import url_for, request

from . import useronly


class Tab:

    def __init__(self, name, url):
        self.name = name
        self.url  = url

    def is_current(self):
        '''true if this tab is the current tab'''
        if request.view_args is None:
            return False    # otherwise error.blueprint will throw and error
        return url_for(request.endpoint, **request.view_args)==self.url

    def before_current(self):
        '''true if this tab is before the current tab'''
        tab_after = Navigation.get_after(self)
        return tab_after.is_current() if tab_after else False

    def after_current(self):
        '''true if this tab is after the current tab'''
        tab_before = Navigation.get_before(self)
        return tab_before.is_current() if tab_before else False


class Navigation:

    default = [
        Tab('Home'         , '/'           ),
        Tab('Register'     , '/register'   ),
        Tab('Log in'       , '/login'      ),
        # Tab('Suggestions'  , '/suggestions'),
        Tab('Our Catalogue', '/catalogue'  ),
        Tab('About Us'     , '/aboutus'    ),
        Tab('Custom 404'   , '/doesntexist'),
    ]

    authenticated = [
        Tab('Home'         , '/'           ),
        Tab('Account'      , '/account'    ),
        Tab('Log out'      , '/logout'     ),
        Tab('Social'       , '/social'     ),
        # Tab('Suggestions'  , '/suggestions'),
        Tab('Our Catalogue', '/catalogue'  ),
        Tab('About Us'     , '/aboutus'    ),
    ]

    def __getitem__(self, idx):
        return self.authenticated[idx] if useronly.verify() \
          else self.default[idx]

    @classmethod
    def offset_tab(cls, tab, offset):
        if tab not in cls.default and tab not in cls.authenticated:
            raise ValueError(f'<Tab {tab.name}> not in Navigation')
        tabs = cls.default if tab in cls.default else cls.authenticated
        idx = tabs.index(tab)+offset
        if 0<=idx<len(tabs): return tabs[idx]

    @classmethod
    def get_before(cls, tab):
        '''get the tab before the specified tab'''
        return cls.offset_tab(tab, -1)

    @classmethod
    def get_after(cls, tab):
        '''get the tab before the specified tab'''
        return cls.offset_tab(tab, +1)

    def first_current(self):
        '''true if the first tab is the current tab'''
        return self[0].is_current()

    def last_current(self):
        '''true if the last tab is the current tab'''
        return self[-1].is_current()
