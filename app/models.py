from django.db import models

# Create your models here.
class Alunos(models.Model):
    pasta = models.IntegerField()
    ano = models.DateField()
    nome = models.CharField(max_length=150)
    filiacao = models.CharField(max_length=100)