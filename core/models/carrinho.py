from django.db import models

from .ingresso import Ingresso


class Carrinho(models.Model):
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


