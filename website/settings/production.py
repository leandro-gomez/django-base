from .base import *

PROD_MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # https://warehouse.python.org/project/whitenoise/
]
MIDDLEWARE = MIDDLEWARE + PROD_MIDDLEWARE

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
