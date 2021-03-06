from .base import *

PROD_MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # https://warehouse.python.org/project/whitenoise/
]
MIDDLEWARE = MIDDLEWARE + PROD_MIDDLEWARE

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ALLOWED_HOSTS_RAW = env("ALLOWED_HOSTS")
ALLOWED_HOSTS = ALLOWED_HOSTS_RAW.split(",")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "django_default_cache"),
    }
}

#  FULL NAME,email@example.com;FULL NAME2,email2@example.com
ADMINS_RAW = env("ADMINS", default=None)
if ADMINS_RAW:
    ADMINS = [full_name__email.split(",") for full_name__email in ADMINS_RAW.split(";")]

#  FULL NAME,email@example.com;FULL NAME2,email2@example.com
MANAGERS_RAW = env("MANAGERS", default=None)
if MANAGERS_RAW:
    MANAGERS = [full_name__email.split(",") for full_name__email in MANAGERS_RAW.split(";")]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = "DENY"
