# django-base

[![django-base](https://circleci.com/gh/leandro-gomez/django-base.svg?style=svg)](https://app.circleci.com/pipelines/github/leandro-gomez/django-base)

[![codecov](https://codecov.io/gh/leandro-gomez/django-base/branch/main/graph/badge.svg?token=VAPRPUG6AN)](https://codecov.io/gh/leandro-gomez/django-base)

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

## Integration tests

- Google Chrome
- Firefox
- Download a [chromedriver](https://chromedriver.chromium.org/downloads)
  - `wget "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(google-chrome --version | awk '{print $3}' | awk -F \. '{print $1}')" -O drivers/google_driver_version.txt`
  - `wget -N "https://chromedriver.storage.googleapis.com/$(cat drivers/google_driver_version.txt)/chromedriver_linux64.zip" -O drivers/chromedriver.zip`
  - `unzip drivers/chromedriver.zip -d drivers/`
  - `chmod +x drivers/chromedriver`
- Download a [geckodriver](https://github.com/mozilla/geckodriver/releases)
  - `wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz -O drivers/geckodriver.tar.gz`
  - `tar zxvf drivers/geckodriver.tar.gz -C drivers/`
  - `chmod +x drivers/geckodriver`
- Run `pytest --driver Firefox --driver-path drivers/geckodriver --base-url localhost:8000 integration_tests/`
- Run `pytest --driver Chrome --driver-path drivers/chromedriver --base-url localhost:8000 integration_tests/`

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


### Heroku

- https://devcenter.heroku.com/articles/django-assets
