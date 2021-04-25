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

ADMINS = [(full_name, email) for full_name, email in env("ADMINS", default=",").split(",")]
MANAGERS = [(full_name, email) for full_name, email in env("MANAGERS", default=",").split(",")]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
