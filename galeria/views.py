from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    print('Request type:', request.method)
    print(HttpResponse)

    return HttpResponse('<h1>Olá, mundo!</h1>')
