from django.db import models

from .categoria import Categoria


class Filme(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.IntegerField()
    categoria = models.ManyToManyField(Categoria)
    dataLancamento = models.IntegerField()
    sinopse = models.TextField()
    trailer = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.nome