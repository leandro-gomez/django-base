"""
Common app views
"""
from django.shortcuts import render


def index(request):
    """
    Index view rendering the site title
    """
    return render(template_name="common/index.html", request=request, context={})
