from django.urls import path
from usuarios.views import *


urlpatterns = [
    path('login/', login_user, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('buscar/', buscar, name='buscar'),
]
