from django.shortcuts import render


def index(request):

    print('Request TYPE:', request.method)

    return render(request, 'galeria/index.html')


def imagem(request):

    print('Request IMAGEM TYPE:', request.method)

    return render(request, 'galeria/imagem.html')