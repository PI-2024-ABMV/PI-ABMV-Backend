from django.db import models


class Sala(models.Model):
    numeroAssentos = models.IntegerField(null=False, blank=False, default=0)
    numeroSala = models.IntegerField(null=False, blank=False, default=0)