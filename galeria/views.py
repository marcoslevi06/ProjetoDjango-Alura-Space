from django.shortcuts import render
from galeria.models import *

def index(request):

    print('Request TYPE:', request.method)

    fotografia = Fotografia.objects.all()
    print('Fotografia:', fotografia)

    # for f in fotografia:
    #     print(f.nome, f.legenda, f.descricao, f.foto)

    return render(request, 'galeria/index.html', {'fotografia': fotografia})


def imagem(request):

    print('Request IMAGEM TYPE:', request.method)

    return render(request, 'galeria/imagem.html')