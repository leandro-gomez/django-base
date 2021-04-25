from .base import *

PROD_MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # https://warehouse.python.org/project/whitenoise/
]
MIDDLEWARE = MIDDLEWARE + PROD_MIDDLEWARE

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ALLOWED_HOSTS = [
    "django-base-7337.herokuapp.com",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "django_default_cache"),
    }
}

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

ADMINS = [(full_name, email) for full_name, email in env("ADMINS", default=",").split(",")]
MANAGERS = [(full_name, email) for full_name, email in env("MANAGERS", default=",").split(",")]
