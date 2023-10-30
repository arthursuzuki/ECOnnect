from django.contrib.auth.models import User
from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField(max_length=500)

class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    celular = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)