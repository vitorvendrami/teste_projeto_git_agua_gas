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


def minhas_informacoes(request):  # Mostra os dados do usuário que está logado.
    if request.user.is_authenticated:
        usuario = request.user

        nome = usuario.nome
        email = usuario.email
        senha = usuario.senha

        return render(request, 'minhas_informacoes.html', {'nome': nome, 'email': email, 'senha': senha})


@csrf_protect
def comprar_livro(request, nome):
    if request.user.is_authenticated:
        usuario = request.user

        livro = Livro.objects.filter(nome=nome).first()
        if livro:
            usuario.livros.add(livro)

        livros = usuario.livros
        return render(request, 'meus_livros.html', {'livros': livros})


@csrf_protect
def meus_livros(request):  # Retorna a lista de livros do usuário que está logado.
    if request.user.is_authenticated:
        usuario = request.user
        livros = usuario.livros

        return render(request, 'meus_livros.html', {'livros': livros})


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
def livros_venda(request):  # Mostra a lista de livros.
    livros = Livro.objects.all()
    return render(request, 'menu.html', {'livros': livros})

def configuracoes(request):
    return render(request, 'Cadastrar.html')

def consulta_livros(request):
	consulta = request.POST.get('consulta')
	campo = request.POST.get('campo')


	titulo = 'Listagem de Pessoas'
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

