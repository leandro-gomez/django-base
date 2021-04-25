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
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, "django_default_cache"),
    }
}
