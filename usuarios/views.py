from django.shortcuts import render

# Create your views here.

def login_user(request):

    return render(request, 'usuarios/login.html')

def cadastro(request):

    return render(request, 'usuarios/cadastro.html')

def buscar(request):
    
        return render(request, 'usuarios/buscar.html')