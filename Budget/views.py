from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def orcamento(request):
    return render(request, 'global/orcamento.html', context={
        'name': 'Cálculo Orçamento'
    })

def home(request):
    return render(request, 'global/home.html', context={
        'name': 'ECONNECT'
    })


def area(request):
    return render(request, 'global/area.html', context={
        'name': 'Área Disponível'
    })


def potencial(request):
    return render(request, 'global/potencial.html', context={
        'name': 'Potencial de Geração de Energia'
    })


def calculadora(request):
    return render(request, 'global/calculadora.html', context={
        'name': 'Cálculo Orçamento'
    })

def infocredito(request):
    return render(request, 'global/infocredito.html', context={
        'name': 'Créditos de Carbono'
    })

def login(request):
    return render(request, 'global/login.html', context={
        'name': 'Login'
    })

def cadastro(request):
    return render(request, 'global/cadastro.html', context={
        'name': 'Cadastro'
    })

def informacaosolar (request):
    return render(request, 'global/informacaosolar.html', context={
        'name': 'Informação Solar'
    })


def suporte(request):
    return HttpResponse('Suporte')


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def informacoes(request):
    return HttpResponse('Informações')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')
