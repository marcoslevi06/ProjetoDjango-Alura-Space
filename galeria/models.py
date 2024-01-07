from django.db import models
from datetime import datetime
# Create your models here.


class Fotografia(models.Model):

    nome = models.CharField(max_length=200, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    foto = models.CharField(max_length=200, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'{self.nome} - {self.legenda}'
