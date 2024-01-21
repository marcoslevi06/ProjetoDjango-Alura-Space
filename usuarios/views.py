from django.shortcuts import render, redirect
from usuarios.forms import *
# importando o model de usuarios (tabela do banco de dados)
from django.contrib.auth.models import User
# importando o modulo de autenticação
from django.contrib import auth
# impotando mensagens de erro
from django.contrib import messages


def login_user(request):

    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            sucesso = False

            # verifica se o usuario existe
            if User.objects.filter(username=nome, password=senha).exists():
                sucesso = True
                return redirect('login')

            # atutentica o usuario
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(
                    request, f'{nome} Login realizado com sucesso!')
                return redirect('login')
            else:
                messages.error(request, 'Login ou senha incorretos!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):

    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

    if form.is_valid():

        if form['senha_1'].value() != form['senha_2'].value():
            messages.error(request, 'Senhas não conferem!')
            return render(request, 'usuarios/cadastro.html')

        nome = form['nome_cadastro'].value()
        email = form['email'].value()
        senha = form['senha_1'].value()

        print(f'Nome: {nome}')
        print(f'Email: {email}')
        print(f'Senha: {senha}')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return render(request, 'usuarios/cadastro.html')

        novo_usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )

        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})


def buscar(request):

    return render(request, 'usuarios/buscar.html')


def logout(request):
    messages.success(request, 'Logout realizado com sucesso!')
    auth.logout(request)
    return redirect('login')
