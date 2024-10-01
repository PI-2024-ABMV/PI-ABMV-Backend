from django.db import models

from .categoria import Categoria

class Filme(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    dataLancamento = models.IntegerField()
    sinopse = models.TextField()
    trailer = models.URLField()
    

    def __str__(self):
        return self.nome