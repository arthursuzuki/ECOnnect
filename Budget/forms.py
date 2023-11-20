from django import forms
from django.forms import TextInput

from .models import Contato, Empresas, Feedback


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'celular', 'email', 'mensagem']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nome', 'sobrenome','cidade','estado', 'nota', 'texto']


class EmpresasProxForm(forms.ModelForm): ##Novooo
    class Meta:
        model = Empresas
        fields = ['nome', 'rua']



