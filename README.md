# django-base

## Requirements

- [Docker](https://www.docker.com/)
- [Docker compose](https://docs.docker.com/compose/)
- [pyenv](https://github.com/pyenv/pyenv)

## Setup

- `git clone git@github.com:leandro-gomez/django-base.git;`
- `cd django-base;`
- `pyenv install 3.9.4`
- `pyenv virtualenv 3.9.4 django-base`
- `pip install -r requirements/local.txt`

## Development

- Init database: `./manage.py migrate`
- Run local server: `./manage.py runserver 0.0.0.0:8000`
- Run tests: `pytest`
