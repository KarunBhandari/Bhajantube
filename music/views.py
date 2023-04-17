from django.http import HttpResponse
from django.shortcuts import render

from music.models import Songs


def index(request):
    return render(request, 'index.html')
