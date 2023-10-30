from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContatoForm, Perfil
from .models import *


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

'''def login(request):
    return render(request, 'global/login.html', context={
        'name': 'Login'
    })

def cadastro(request):
    return render(request, 'global/cadastro.html', context={
        'name': 'Cadastro'
    })'''

def cadastro(request):
    if request.method == 'POST':
        form = Perfil(request.POST)
        if form.is_valid():
            form.save()
            return redirect('global/home.html')
    else:
        form = Perfil()
    return render(request,"global/cadastro.html",{'form':form})

def informacaosolar(request):
    roi = None

    if request.method == 'POST':
        tipo_local = request.POST.get('tipo_local')
        gasto_mensal = float(request.POST.get('gasto_mensal').replace('R$', '').replace(',', '').strip())

        if tipo_local == 'Residencial':
            custo_instalacao = 5000
        elif tipo_local == 'Comercial':
            custo_instalacao = 10000
        elif tipo_local == 'Industrial':
            custo_instalacao = 20000
        else:
            return HttpResponse("Tipo de local inválido.")

        economia_anual = gasto_mensal * 12

        if custo_instalacao > 0:
            roi = (economia_anual / custo_instalacao) * 100
        else:
            roi = 0

    return render(request, 'global/informacaosolar.html', {'name': 'Informação Solar', 'roi': roi})

def faq(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request,"global/faq.html",{'form':form})


def suporte(request):
    return HttpResponse('Suporte')


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def informacoes(request):
    return HttpResponse('Informações')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')
