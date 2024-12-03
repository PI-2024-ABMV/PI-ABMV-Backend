from django.db import models

from .ingresso import Ingresso


class Carrinho(models.Model):
    quantidade = models.IntegerField()
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)