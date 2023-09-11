# models.py
from django.db import models

class Sedimentacao(models.Model):
    processo = models.CharField(max_length=255)
    capacidade = models.IntegerField()
    nivel_tanque = models.CharField(max_length=255)
    etapa = models.CharField(max_length=255)
    viscosidade = models.CharField(max_length=255)
    tempo_estimado = models.CharField(max_length=255)

    def __str__(self):
        return self.processo