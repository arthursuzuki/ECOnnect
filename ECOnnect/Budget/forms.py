from django import forms

from .models import Contato, Feedback, InfoCreds


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'celular', 'email', 'mensagem']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nome', 'sobrenome','cidade','estado', 'nota', 'texto']


class InfoCredsForm(forms.ModelForm):
    class Meta:
        model = InfoCreds
        fields = ['creditos']