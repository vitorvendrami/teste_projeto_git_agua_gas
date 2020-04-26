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
    dado = Dado.objects.all()
    usuario.save()

    return render(request, 'menu.html', {'dados':dado})

@csrf_protect
def login(request):
    return render(request, 'login.html')

@csrf_protect
def confirmar_login(request):
    nome = request.POST.get('inputEmailLogin')
    senha = request.POST.get('inputPasswordLogin')

    dados = Dado.objects.all()

    usuario = Dado.objects.filter(nome=nome)

    if usuario.senha == senha:
        return render(request, 'menu.html')

    print(usuario)
    return render(request, 'login.html')
