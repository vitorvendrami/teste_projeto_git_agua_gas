from django.urls import path
from .views import *

urlpatterns = [
    path('', login),
    path('nosso_site/login', login),
    path('site_teste/confirmar_login/', confirmar_login),
    path('nosso_site/cadastro', cadastro),
    path('site_teste/confirmar_cadastro/', confirmar_cadastro)



]
