from django.db import models


class Livro(models.Model):
	nome = models.CharField(max_length=80)
	nPaginas = models.IntegerField()
	autor = models.CharField(max_length=70)
	categoria = models.CharField(max_length=50, default='Geral')
	# preco = models.CharField(max_length=7)

	def __str__(self):
		return self.nome


class Dado(models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	senha = models.CharField(max_length=15)
	livros = models.ManyToManyField(Livro)
	# saldo = models.CharField(max_length=7, default='200.00')

	def __str__(self):
		return self.nome
