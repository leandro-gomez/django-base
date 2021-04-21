"""
Common context processors
"""
from django.conf import settings


def global_settings(_):
    """
    Set some settings into context from django settings
    """
    return {
        "SITE_TITLE": settings.SITE_TITLE,
    }
