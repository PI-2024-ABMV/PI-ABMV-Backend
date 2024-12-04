from django.db import models

from .filme import Filme
from .sala import Sala


class Sessao(models.Model):
    horario = models.DateTimeField(null=False, blank=False)
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)