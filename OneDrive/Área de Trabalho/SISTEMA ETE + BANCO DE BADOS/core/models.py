# models.py

from django.db import models
from django.contrib.auth.models import User

class HistoricoAtivacao(models.Model):
    ativo = models.CharField(max_length=255)
    acao = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ativo} - {self.acao}"

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
