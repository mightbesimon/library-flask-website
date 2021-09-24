''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157
'''

import pytest
from flask import session

from config  import TestingConfig
from library import create_app


@pytest.fixture
def client():
    app = create_app(TestingConfig)
    return app.test_client()


def credentials(client, url, username, password):
    return client.post(url, data={
        'username': username,
        'password': password
    })

class TestRegistration:

    def test_response_code(self, client):
        assert 200 == client.get('/register').status_code

    def test_valid_input(self, client):
        response = credentials(client, '/register', 'shakespeare', 'Password1')
        assert 'http://localhost/account' == response.headers['Location']

    def test_invalid_input(self, client):
        response = credentials(client, '/register', ' ', 'Password1')
        assert b'A username is required for registration' in response.data

        response = credentials(client, '/register', '12345', 'Password1')
        assert b'That username is too short' in response.data

        response = credentials(client, '/register', 'jamesbond', 'Password1')
        assert b'That username is taken' in response.data
        assert b'do you want to login?' in response.data

        response = credentials(client, '/register', 'shakespeare', ' ')
        assert b'A password is required for registration' in response.data

        response = credentials(client, '/register', 'shakespeare', '12345')
        assert b'That password is too short' in response.data

        response = credentials(client, '/register', 'shakespeare', 'abcdef')
        assert b'Your password needs a digit' in response.data

        response = credentials(client, '/register', 'shakespeare', 'abc123')
        assert b'Your password needs an upper case character' in response.data

        response = credentials(client, '/register', 'shakespeare', 'ABC123')
        assert b'Your password needs a lower case character' in response.data


class TestLogin:

    def test_response_code(self, client):
        assert 200 == client.get('/login').status_code

    def test_valid_input(self, client):
        response = credentials(client, '/login', 'julius-caesar', 'password')
        assert 'http://localhost/account' == response.headers['Location']

        # test a session is created
        with client:
            client.get('/')
            assert session['username'] == 'julius-caesar'

    def test_invalid_input(self, client):
        response = credentials(client, '/login', ' ', 'password')
        assert b'A username is required for logging in' in response.data

        response = credentials(client, '/login', 'aliens', 'password')
        assert b'That username doesn' in response.data
        assert b't exist' in response.data
        assert b'do you want to register?' in response.data

        response = credentials(client, '/login', 'jamesbond', ' ')
        assert b'A password is required for logging in' in response.data

        response = credentials(client, '/login', 'test', 'password')
        assert b'Incorrect password' in response.data


class TestLogout:

    def test_response_code(self, client):
        response = client.get('/logout')
        assert 302 == response.status_code
        assert 'http://localhost/' == response.headers['Location']

    def test_session_cleared(self, client):
        with client:
            client.get('/logout')
            assert 'username' not in session


class TestAuthorisation:

    def test_account(self, client):
        response = client.get('/account')
        assert 'http://localhost/login' == response.headers['Location']

    def test_mark_as_read(self, client):
        response = client.get('/book/25742454/read')
        assert 'http://localhost/login' == response.headers['Location']

    def test_write_review(self, client):
        response = client.get('/book/25742454/review')
        assert 'http://localhost/login' == response.headers['Location']


def write_review(client, url, rating, review_text):
    return client.post(url, data={
        'rating': rating,
        'text'  : review_text,
    })

class TestWriteReview:

    def test_valid_review(self, client):
        credentials(client, '/login', 'julius-caesar', 'password')
        response = write_review(client, '/book/25742454/review', 5, 'good')
        assert 'http://localhost/book/25742454' == response.headers['Location']

    def test_valid_review(self, client):
        credentials(client, '/login', 'julius-caesar', 'password')
        response = write_review(client, '/book/25742454/review', None, 'good')
        assert b'A rating is required for a review' in response.data


class TestSearch:

    def test_short_search(self, client):
        # test no input title
        response = client.post('/catalogue')
        assert 302 == response.status_code
        assert 'http://localhost/catalogue/search' == response.headers['Location']

        # test with input title
        response = client.post('/catalogue', data={'title': 'the'})
        assert 302 == response.status_code
        assert 'http://localhost/catalogue/search?title=the' == response.headers['Location']

    def test_search_title(self, client):
        response = client.get('/catalogue/search?title=the')
        assert 200 == response.status_code

    def test_search_author(self, client):
        response = client.get('/catalogue/search?author=Asma')
        assert 200 == response.status_code

    def test_search_year(self, client):
        response = client.get('/catalogue/search?year=2021')
        assert 200 == response.status_code

    def test_search_publisher(self, client):
        response = client.get('/catalogue/search?publisher=Marvel')
        assert 200 == response.status_code
