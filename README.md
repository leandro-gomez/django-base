# django-base

[![django-base](https://circleci.com/gh/leandro-gomez/django-base.svg?style=svg)](https://app.circleci.com/pipelines/github/leandro-gomez/django-base)


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
- `cp website/settings/.env.local website/settings/.env`

## Development

- Start database: `docker-compose up -d db`
- Run migrations: `./manage.py migrate`
- Run local server: `./manage.py runserver 0.0.0.0:8000`
- Run tests: `pytest --cov`
- Linting
    - prospector: `prospector`
    - black: `black website --check`

## Production

**NOTE: DO NOT USE website/settings/.env.local FILE!**

Set environment variables on `website/settings/.env`:

```
SECRET_KEY="your_secret_key"
DATABASE_URL="connection_string"
DEBUG=0
```

Run gunicorn `gunicorn -c website/gunicorn.py website.wsgi:application`
**TIP:** Use `-w` for tuning the amount of gunicorn workers 
