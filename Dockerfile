FROM python:3.9.4-buster

ARG requirements=requirements/production.txt
ENV DJANGO_SETTINGS_MODULE=website.settings.production

COPY requirements/ requirements/
COPY website/ website/
COPY manage.py .

RUN pip3 install -U pip && pip3 install -r $requirements

CMD ['gunicorn', '-c', 'website/gunicorn.py']
