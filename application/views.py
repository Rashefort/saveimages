from django.shortcuts import render
from .models import User


def create(request, url):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    user = User.objects.create(ip=ip, url=url)
    user.save()


def general(request):
    create(request, request.path)
    return render(request, 'application/general.html', {})


def address(request, slug):
    create(request, slug)
    return render(request, 'application/general.html', {})
