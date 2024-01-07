from django.shortcuts import render


def index(request):

    print('Request TYPE:', request.method)

    return render(request, 'galeria/index.html')
