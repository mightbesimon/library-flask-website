''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

### authorisation policies ###

from .authorisation import Policy
from ..adapters import _repo

useronly = Policy(session_key='username',
        verification_function=_repo.username_exists)


### nagivation sidebar ###

from .navigation import Navigation
nav = Navigation()


#======[!] * * *   help with imports   * * * [!]======#
from .form_registration import RegistrationForm
from .form_login        import LoginForm
from .authorisation     import authorisation
from .form_review       import ReviewForm
from .form_search       import SearchTitleForm, SearchForm
#======[!] * * *   help with imports   * * * [!]======#
