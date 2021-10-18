# Assignment Two Repository

> COMPSCI 235 (2021) - University of Auckland  
> ASSIGNMENT PHASE TWO  
> Simon Shan  441147157

- [Description](#description)
- [Structure](#structure)
- [Requirements](#requirements)
- [Automated Tests](#automated-tests)
- [Executing the web application](#executing-the-web-application)
- [Data sources](#data-sources)

## Description ##

This repository contains an implementation of the domain model from Assignment 1. 
It contains unit tests which can be run through pytest. 
It also contains a simple Flask application that renders content of a Book object instance from our domain model.

### Notes

- Services are called handlers in this project.
- Pleasent webpage aesthetics and user experience.
  - [x] Copyright information in the footer at the bottom of the page.
  - [x] Nav sidebar shows a bookmark for the current page and ...
  - [x] The tabs just above and below the current tab is rounded off.
  - [x] Registration and login pages look like the user is filling out a library card.
  - [x] Custom 404 page.
- Testing
  - [x] Unit tests (models).
  - [x] Unit tests (adapters).
  - [x] Unit tests (handlers).
  - [x] Intergration tests.
- Search feature
  - [x] Search books by title at `/catalogue`, which redirects you to ...
  - [x] Advanced search page`/catalogue/search` where you can search by author, release year and publisher.
  - if you do not wish to search by title, click on the search button without a title on the catalogue page, it will redirect you to the advanced search page.
  - [x] Http query parameters
- Cool new features
  - [x] New image_url and language attributes to `Book` model.
  - [x] LINQ support.
  - [x] Policy-based authorisation.
  - [x] Salt hashes passwords for security.
  - [x] Personalised suggestions.
  - [x] Social page, follow other users.

## Structure ##

```
compsci235-assignment2-covid-19/
│
├──📁 .git/
│   └── ...
├──📁 .github/
│   └── ...
├──⚙️ .gitignore
├──📁 venv/
│   └── ...
│
├──📦 library/
│   │
│   ├──📁 data/
│   │   ├──🗂 book_authors_excerpt.json
│   │   ├──🗂 comic_books_excerpt.json
│   │   └──🗂 dummy_users_and_reviews.json
│   ├──📦 models/
│   │   ├──📄 __init__.py
│   │   ├──📄 publisher.py
│   │   ├──📄 author.py
│   │   ├──📄 book.py
│   │   ├──📄 review.py
│   │   ├──📄 user.py
│   │   └──📄 inventory.py
│   │
│   ├──📦 adapters/
│   │   ├──📄 __init__.py
│   │   ├──📄 jsondatareader.py
│   │   ├──📄 dataset.py
│   │   ├──📄 memory_datacontext.py
│   │   ├──📄 abstract_repository.py
│   │   └──📄 memory_repository.py
│   ├──📦 blueprints/
│   │   ├──📄 __init__.py
│   │   ├──📄 home.py
│   │   ├──📄 authentication.py
│   │   ├──📄 account.py
│   │   ├──📄 catalogue.py
│   │   └──📄 error.py
│   ├──📦 handlers/
│   │   ├──📄 __init__.py
│   │   ├──📄 authorisation.py
│   │   ├──📄 form_register.py
│   │   ├──📄 form_login.py
│   │   ├──📄 form_review.py
│   │   ├──📄 form_search.py
│   │   └──📄 navigation.py
│   │
│   ├──📁 static/
│   │   ├──🏞 about.png
│   │   ├──🏞 login.png
│   │   ├──🏞 register.png
│   │   ├──🏞 favicon.ico
│   │   ├──🏞 notfound.gif
│   │   ├──📄 home.css
│   │   └──📄 style.css
│   ├──📁 templates/
│   │   ├──📄 aboutus.html
│   │   ├──📄 home.html
│   │   │
│   │   ├──📄 credentials.html
│   │   ├──📄 account.html
│   │   ├──📄 social.html
│   │   │
│   │   ├──📄 catalogue.html
│   │   ├──📄 book_info.html
│   │   │
│   │   ├──📄 layout.html
│   │   ├──📄 navigation.html
│   │   └──📄 notfound.html
│   │
│   └──📄 __init__.py
│
├──📁 tests/
│   ├──📁 intergration/
│   │   └──🧪 test_end2end.py
│   └──📁 unit/
│       ├──🧪 test_adapters.py
│       ├──🧪 test_handlers.py
│       └──🧪 test_models.py
│
│
├──⚙️ requirements.txt
├──📚 structure.txt
├──📚 README.md
│
├──⚙️ .env
├──⚙️ config.py
├──📄 utils.py
└──📄 wsgi.py
```

### Changes

- moved `data/` out of `adapters/`, so it is now `library/data`/ instead of `library/adapters/data/`
- broken up `model.py` into individual files.
- renamed `library/domain/model.py` to `library/models`
- renamed `tests/unit/test_domain_model` to `tests/unit/test_models`
- renamed `services` to `handlers`
- blueprints and handlers are separated into 2 folders, `blueprints/` and `handlers/`


## Requirements ##

Please use Python version 3.6 or newer versions for development. Some of the depending libraries of our web application do not support Python versions below 3.6!

### Virtual Environment

All commands for testing or execution should be run inside the virtual environment.

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

To deactivate the virtual environment, do:

```bash
$ deactivate
```

### Automated Tests

From the root directory of the project
```bash
$ python -m pytest tests
```
### Executing the web application

From the root directory

````bash
$ flask run
````

## Data sources 

The data in the excerpt files were downloaded from (Comic & Graphic):
https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home

On this webpage, you can find more books and authors in the same file format as in our excerpt, for example for different book genres. 
These might be useful to extend your web application with more functionality.

We would like to acknowledge the authors of these papers for collecting the datasets by extracting them from Goodreads:

*Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18.*

*Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19.*

## Authors ##

- COMPSCI 235 staff | University of Auckland &mdash; initial skeleton code
- Simon | [mightbesimon](github.com/mightbesimon) &mdash; everything else (Copyright 2021 mightbesimon)

## Licence ##
`dataset.py`, `authorisation.py`, `style.css`, `home.css`, `structure.txt`: All rights reserved. [mightbesimon](github.com/mightbesimon) 2021  
Everything else: MIT

