from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', index, name='index'),
    # nome da rota, função que será executada(nome da View), name='nome da rota'
    path('imagem/<int:foto_id>', imagem, name='imagem'),
]
