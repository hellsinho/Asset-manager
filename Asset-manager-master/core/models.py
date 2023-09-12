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

class dados(models.Model):

    dado = models.CharField(max_length=100)
    def __str__(self):
        return self.dado
    
class dados1(models.Model):

    dado1 = models.CharField(max_length=100)
    def __str__(self):
        return self.dado1
    
class dados2(models.Model):

    dado2 = models.CharField(max_length=100)
    def __str__(self):
        return self.dado2
    
class dados3(models.Model):

    dado3 = models.CharField(max_length=100)
    def __str__(self):
        return self.dado3
