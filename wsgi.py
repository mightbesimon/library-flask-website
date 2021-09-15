''' COMPSCI 235 (2021) - University of Auckland
    ASSIGNMENT PHASE TWO
    Simon Shan  441147157

    Flask app entry point
'''

from library import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000, 
        threaded=False,
    )
