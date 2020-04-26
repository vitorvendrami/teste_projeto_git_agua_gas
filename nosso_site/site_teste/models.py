from django.db import models


class Dado(models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	senha = models.CharField(max_length=15)

	def __str__(self):
		return self.nome


class Livro(models.Model):
	nome = models.CharField(max_length=80)
	nPaginas = models.IntegerField()
	autor = models.CharField(max_length=70)

	def __str__(self):
		return self.nome
