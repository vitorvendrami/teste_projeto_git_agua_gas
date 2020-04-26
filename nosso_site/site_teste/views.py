from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Dado


def cadastro(request):
    return render(request, 'Cadastrar.html')


@csrf_protect
def confirmar_cadastro(request):
    nome = request.POST.get('inputNameCadastro')
    email = request.POST.get('inputEmail3Cadastro')
    senha = request.POST.get('inputPasswordCadastro')

    usuario = Dado(
        nome=nome,
        email=email,
        senha=senha
    )
    usuario.save()

    return render(request, 'Cadastrar.html')


def login(request):
    return render(request, 'login.html')


def confirmar_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    usuario = Dado.objects.filter(nome=nome)

    if usuario and usuario.senha == senha:
        return render(request, 'menu.html')

    return render(request, 'login.html')
