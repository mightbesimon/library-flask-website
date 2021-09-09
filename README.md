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
It also contains a simple Flask application that renders content of a Book object instance from our domain model on a blank html page.

Please note that this sample implementation from Assignment 1 contains a more comprehensive superset of tests compared with what we had as hidden tests on Coderunner. 
Your domain model implementation may have to be extended to meet all test cases in the sample implementation, but you may also decide to remove or modify test cases as it suits you. 
From here on you can choose if you want to use the provided domain model or your implementation, just make sure your chosen set of test cases always work with your implementation.

## Structure ##

```
compsci235-assignment2-covid-19/
├── .github/
│   └── ...
├── .gitignore
├── library/
│   ├── adapters/
│   │   ├── __init__.py
│   │   ├── jsondatareader.py
│   │   ├── DataSet.py
│   │   ├── LibraryDataContext.py
│   │   ├── IRepository.py
│   │   └── LibraryRepository.py
│   ├── data/
│   │   ├── book_authors_excerpt.json
│   │   └── comic_books_excerpt.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── publisher.py
│   │   ├── author.py
│   │   ├── book.py
│   │   ├── review.py
│   │   └── user.py
│   ├── blueprints/
│   │   └── ...
│   ├── services/
│   │   └── ...
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── ...
│   │   ├── layout.html
│   │   └── navigation.html
│   └── __init__.py
├── tests/
│   ├── ...
│   └── unit/
│       ├── test_adapters.py
│       └── test_domain_model.py
├── venv/
│   └── ...
├── requirements.txt
├── README.md
├── .env
├── config.py
├── utils.py
└── wsgi.py
```

### Changes

- moved `data/` out of `adapters/`, so it is now `library/data`/ instead of `library/adapters/data/`
- broken up `model.py` into individual files.
- renamed `library/domain/model.py` to `library/models`


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
`DataSet.py`: All rights reserved. [mightbesimon](github.com/mightbesimon) 2021  
Everything else: MIT

