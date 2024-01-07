from django.shortcuts import render, get_object_or_404
from galeria.models import *

def index(request):

    print('Request TYPE:', request.method)

    fotografia = Fotografia.objects.all()

    # cont = 0
    # for foto in fotografia:
    #     cont += 1
    #     print(f'Fotografia {cont}: {foto.nome} - {foto.legenda} - {foto.descricao} - {foto.foto}')

    return render(request, 'galeria/index.html', {'fotografia': fotografia})


def imagem(request, foto_id):

    print('Request IMAGEM TYPE:', request.method)
    print('Request IMAGEM ID:', foto_id)

    foto = get_object_or_404(Fotografia, pk=foto_id)

    print(f'Foto: {foto.nome} - {foto.legenda} - {foto.descricao} - {foto.foto}')

    return render(request, 'galeria/imagem.html', {'foto': foto})