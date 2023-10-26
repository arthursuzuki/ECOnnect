from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContatoForm


# Create your views here.
def orcamento(request):
    return render(request, 'orcamento.html', context={
        'name': 'Cálculo Orçamento'
    })

def home(request):
    return render(request, 'home.html', context={
        'name': 'ECONNECT'
    })


def area(request):
    return render(request, 'area.html', context={
        'name': 'Área Disponível'
    })


def potencial(request):
    return render(request, 'potencial.html', context={
        'name': 'Potencial de Geração de Energia'
    })


def calculadora(request):
    return render(request, 'calculadora.html', context={
        'name': 'Cálculo Orçamento'
    })

def infocredito(request):
    return render(request, 'infocredito.html', context={
        'name': 'Créditos de Carbono'
    })

def login(request):
    return render(request, 'login.html', context={
        'name': 'Login'
    })

def cadastro(request):
    return render(request, 'cadastro.html', context={
        'name': 'Cadastro'
    })

def informacaosolar (request):
    return render(request, 'informacaosolar.html', context={
        'name': 'Informação Solar'
    })

def faq(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request,"faq.html",{'form':form})


def suporte(request):
    return HttpResponse('Suporte')


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def informacoes(request):
    return HttpResponse('Informações')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')