from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de usuário',
        required=True, max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite seu nome de usuário'
            }
        )
    )
    # widget=forms.PasswordInput -> para esconder a senha
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite sua senha'
            },
        ),
        required=True,
        max_length=10,
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        max_length=100,
        required=True,
        label='Nome de Login',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Pessoa Usuário',
            }
        ),
    )

    email = forms.EmailField(
        max_length=100,
        required=False,
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: pessoa@mail.com',
            }
        ),
    )

    senha_1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite sua senha'
            },
        ),
        required=True,
        max_length=10,
    )

    senha_2 = forms.CharField(
        label='Confirme a sua senha',
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite sua senha'
            },
        ),
        required=True,
        max_length=10,
    )
