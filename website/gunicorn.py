# See https://docs.gunicorn.org/en/stable/settings.html#config-file
# Based on https://github.com/benoitc/gunicorn/blob/01a1c7ca9a76d14a707b2946192ca7278247c2ce/examples/example_config.py
import os
from multiprocessing import cpu_count


def max_workers():
    # See https://docs.gunicorn.org/en/20.0.4/design.html#how-many-workers
    return (cpu_count() * 2) + 1


def app_port():
    return os.environ.get("PORT", "8000")


worker_class = "gevent"

proc_name = "django-base-gunicorn"

bind = "0.0.0.0:%s" % app_port()

workers = max_workers()

max_requests = 5000

max_requests_jitter = 500

raw_env = [
    "DJANGO_SETTINGS_MODULE=%s" % os.environ.get("DJANGO_SETTINGS_MODULE", "website.settings.production"),
]

timeout = 400

# https://docs.gunicorn.org/en/19.9.0/settings.html#errorlog
# Equivalent to --log-file
errorlog = os.environ.get("ERROR_LOG", "-")

accesslog = os.environ.get("ACCESS_LOG", "-")

app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

pythonpath = "%s," % app_path
