from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Dado, Livro


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
    dados = Dado.objects.all()
    usuario.save()

    return render(request, 'menu.html', {'dados': dados})


@csrf_protect
def login(request):
    return render(request, 'login.html')


@csrf_protect
def confirmar_login(request):
    email = request.POST.get('inputEmailLogin')
    senha = request.POST.get('inputPasswordLogin')

    usuario = Dado.objects.filter(email=email).first()

    if usuario.senha == senha:
        return render(request, 'menu.html')

    return render(request, 'login.html')


@csrf_protect
def cadastrar_livro(request):
    nome = request.POST.get('inputNomeLivro')
    nPaginas = request.POST.get('inputNPaginas')
    autor = request.POST.get('inputNomeAutor')

    livro = Livro(
        nome=nome,
        nPaginas=nPaginas,
        autor=autor
    )
    livros = Livro.objects.all()
    livro.Save()

    return render(request, 'menu.html', {'livros': livros})


@csrf_protect
def deletar_livro(request, nome):
    Livro.objects.filter(nome=nome).delete()

    livros = Livro.objects.all()
    return render(request, 'menu.html', {'livros': livros})


@csrf_protect
def listagem(request):  # Mostra a lista de livros
    livros = Livro.objects.all()
    return render(request, 'menu.html', {'livros': livros})
