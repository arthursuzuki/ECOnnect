from django import forms

from .models import *


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'celular', 'email', 'mensagem']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'celular', 'email', 'cpf', 'senha']

class CreditoCarbForm(forms.ModelForm):
    class Meta:
        model = CreditoCarb
        fields = ['resultado']