from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContatoForm, EmpresasProxForm, FeedbackForm
from .models import Empresas, Feedback


# Create your views here.
def orcamento(request):
    return render(request, 'orcamento.html', context={
        'name': 'Cálculo Orçamento'
    })

def home(request):
    # Recupera 4 feedbacks aleatórios do banco de dados com 4 estrelas ou mais
    random_feedbacks = Feedback.objects.filter(nota__gte=4).order_by('?')[:4]
    return render(request, 'home.html', {'feedbacks': random_feedbacks, 'name': 'ECONNECT'})
    
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request,"feedback.html",{'form':form, 'name': 'feedback'})

'''def empresaprox(request):
    return render(request, 'empresaprox.html', context={
        'name': 'Empresa próxima'
    })'''

def empresaprox(request):
    if request.method == 'POST':
        form = EmpresasProxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = EmpresasProxForm()
        return render(request,"empresaprox.html",{'form':form, 'name': 'empresaprox'})


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

    return render(request, 'informacaosolar.html', {'name': 'Informação Solar', 'roi': roi})

def faq(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request,"faq.html",{'form':form})


def simulador(request):
    return render(request, 'simulador.html', context={
        'name': 'Simulador Solar'
    })


def resultados(request):
    roi = None
    tipoLocal = None
    potenciaSelecionada = None
    custoInstalacao = None
    economiaAnual = None
    if request.method == 'POST':
        tipoLocal = request.POST.get('tipoLocal')
        potenciaSelecionada = float(request.POST.get('potenciaSelecionada').replace(' kWp', '').replace(',', '').strip())
        gastoMensal = float(request.POST.get('gastoMensal').replace('R$', '').replace(',', '').strip())
        custos_por_potencia = {
            2: 8960.00,
            4: 14720.00,
            8: 26080.00,
            12: 36240.00,
            30: 84300.00,
            50: 142000.00,
            75: 227250.00,
            150: 441000.00,
            300: 882000.00,
            500: 1525000.00,
            1000: 2920000.00,
            3000: 8730000.00,
            5000: 14200000.00,
        }
        if potenciaSelecionada not in custos_por_potencia:
            return HttpResponse("Potência selecionada inválida.")
        custoInstalacao = custos_por_potencia[potenciaSelecionada]
        economiaAnual = gastoMensal * 12
        if custoInstalacao > 0:
            roi = (economiaAnual / custoInstalacao) * 100
        else:
            roi = 0
    return render(request, 'resultados.html', {'name': 'Resultados do Simulador', 'roi': roi, 'tipoLocal': tipoLocal, 'potenciaSelecionada': potenciaSelecionada, 'custoInstalacao': custoInstalacao})


def suporte(request):
    return HttpResponse('Suporte')


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def informacoes(request):
    return HttpResponse('Informações')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')

####### Tentando adicionar
'''def add_empresas(request):
    if request.method == 'POST':
        form = EmpresasProxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request, 'add_empresas.html', {'form': form})'''
def add_empresas(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        rua = request.POST["rua"]

        # Salvar os dados no banco de dados

        return render(request, "add_empresas.html", {
            "nome": nome,
            "rua": rua
        })
    else:
        return render(request, "add_empresas.html")
