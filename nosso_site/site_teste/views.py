from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Dado, Livro

nome = None


def cadastro(request):  # Ok!
    return render(request, 'Cadastrar.html')


def confirmar_cadastro(request):  # Ok!
    global nome
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
def confirmar_login(request):  # Ok!
    global nome
    email = request.POST.get('inputEmailLogin')
    senha = request.POST.get('inputPasswordLogin')

    usuario = Dado.objects.filter(email=email).first()

    '''
    livro = Livro(  # Se quiser adicionar um livro novo manualmente.
        nome='Harry Potter',
        nPaginas='365',
        autor='JK.Rowling',
        categoria='Fantasia',
    )
    livros = Livro.objects.all()
    livro.save()
    '''

    if usuario and usuario.senha == senha:
        nome = usuario.nome
        # usuario.livros.add(livro) ---> Se quiser adicionar um livro manualmente.
        return render(request, 'menu.html')

    return render(request, 'login.html')


def minhas_informacoes(request):  # Ok!
    global nome
    usuario = Dado.objects.filter(nome=nome).first()

    email = usuario.email
    senha = usuario.senha

    return render(request, 'minhas_informacoes.html', {'nome': nome, 'email': email, 'senha': senha})


@csrf_protect
def comprar_livro(request):
    global nome
    usuario = Dado.objects.filter(nome=nome).first()

    nome_livro = request.POST.get('inputNomeLivro')
    livro = Livro.objects.filter(nome=nome).first()
    if livro:
        usuario.livros.add(livro)

    livros = usuario.livros
    return render(request, 'meus_livros.html', {'livros': livros})


@csrf_protect
def meus_livros(request):  # {% for livro in livros %} não funciona.
    global nome
    usuario = Dado.objects.filter(nome=nome).first()
    if usuario:
        livros = usuario.livros.all

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
def livros_venda(request):  # Ok!
    livros = Livro.objects.all()
    return render(request, 'menu.html', {'livros': livros})


def configuracoes(request):
    return render(request, 'Cadastrar.html')


def consulta_livros(request):
    nome = request.POST.get('consulta')
    categoria = request.POST.get('campo')

    livros = Livro.objects.filter(nome=nome, categoria=categoria)

    return render(request, 'meus_livros.html', {'livros': livros})
