from django.urls import path
from .views import *

urlpatterns = [
    path('', login),
    path('nosso_site/login/', login),
    path('site_teste/confirmar_login/', confirmar_login),
    path('nosso_site/cadastro/', cadastro),
    path('site_teste/confirmar_cadastro/', confirmar_cadastro),
    path('site_teste/listagem/<int:id>', login),
    path('site_teste/edicao/<int:id>', login),
    path('site_teste/delecao/<int:id>', login),
    path('site_teste/meus_livros/', meus_livros),
<<<<<<< HEAD
    path('site_teste/minhas_informacoes/', minhas_informacoes),
    path('site_teste/livros_venda/', livros_venda),
=======
    path('site_teste/minhas_informacoes/',minhas_informacoes),
    path('site_teste/meus_livros/<int:id>',meus_livros),
    path('site_teste/livros_venda/<int:id>',livros_venda),
    path('site_teste/configuracoes/<int:id>',configuracoes),
    path('site_teste/consulta_livros/',consulta_livros),


>>>>>>> 150682cc3cf795a88dccc45df4d06ad1abd253a4
]
