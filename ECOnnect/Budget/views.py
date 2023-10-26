from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContatoForm


# Create your views here.
def orcamento(request):
    return render(request, 'global/orcamento.html', context={
        'name': 'Cálculo Orçamento'
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


def suporte(request):
    return HttpResponse('Suporte')


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def informacoes(request):
    return HttpResponse('Informações')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')

def home(request):
    return render(request, "global/home.html")

def faq(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request,"global/faq.html",{'form':form})
