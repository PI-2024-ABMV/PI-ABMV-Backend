from django.db import models

from .sessao import Sessao


class Ingresso(models.Model):
    codigo = models.IntegerField(null=False, blank=False, unique=True)
    tipo = models.BooleanField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    sessao = models.ForeignKey(Sessao, on_delete=models.PROTECT)