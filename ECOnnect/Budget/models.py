from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField(max_length=500)

class Feedback(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=40)
    cidade = models.CharField(max_length=30)
    ESTADOS_BRASILEIROS = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')]
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS)
    class Nota(models.IntegerChoices):
        UM = 1, '1'
        DOIS = 2, '2'
        TRES = 3, '3'
        QUATRO = 4, '4'
        CINCO = 5, '5'

    nota = models.IntegerField(choices=Nota.choices)
    texto = models.CharField(max_length=700)
