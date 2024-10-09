from django.db import models

from .sala import Sala
from .tipoAssento import TipoAssento


class Assento(models.Model):
    numeroAssento = models.IntegerField(null=False, blank=False, default=0)
    fileira = models.CharField(max_length=1)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    tipoAssento = models.ForeignKey(TipoAssento, on_delete=models.PROTECT)
