from django import forms

from .models import *


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'celular', 'email', 'mensagem']

class Perfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'celular', 'email', 'cpf', 'senha']