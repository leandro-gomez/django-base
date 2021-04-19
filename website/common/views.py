from django.shortcuts import render


def index(request):
    return render(template_name="common/index.html", request=request, context={})
