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

class CreditoCarb(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"Creditos de Carbono para {self.user.nome}: {self.valor}"