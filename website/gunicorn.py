# See https://docs.gunicorn.org/en/stable/settings.html#config-file
# Based on https://github.com/benoitc/gunicorn/blob/01a1c7ca9a76d14a707b2946192ca7278247c2ce/examples/example_config.py
import os
from multiprocessing import cpu_count


def max_workers():
    # See https://docs.gunicorn.org/en/20.0.4/design.html#how-many-workers
    return (cpu_count() * 2) + 1


def app_port():
    return os.environ.get("PORT", "8000")


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

# See https://aws.amazon.com/premiumsupport/knowledge-center/elb-capture-client-ip-addresses/
# https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#http-headers

# %({x-forwarded-for}i)s : Remote ip forwarded by AWS Loadbalancer
# %(h)s : remote address. Actually this is a private ip when using a AWS LoadBalancer
# %(l)s : "-" string
# %(t)s : date of the request
# %(s)s : status
# "%(r)s" : status line (e.g. GET / HTTP/1.1)
# %(q)s : Query string
# %(b)s : response length or '-' (CLF format)
# %(T)s :  request time in seconds
# %(f)s :  referrer
# %(a)s : user agent
# %({x-hw-build-number}i)s : X-HW-BUILD-NUMBER if present
access_log_format = '%({x-forwarded-for}i)s %(h)s %(l)s %(t)s %(s)s "%(r)s" "%(q)s" %(b)s %(T)s "%(f)s" "%(a)s"'

app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

pythonpath = "%s," % app_path
