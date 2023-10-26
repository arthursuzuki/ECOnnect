from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField(max_length=500)