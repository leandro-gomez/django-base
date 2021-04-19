from django.conf import settings


def global_settings(_):
    return {
        "SITE_TITLE": settings.SITE_TITLE,
    }
