from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


from .forms import ContatoForm, EmpresasProxForm, FeedbackForm, RoiForm
from .models import Empresas, Feedback, Roi


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

def empresaprox(request):
  empresas = Empresas.objects.all()
  return render(request, 'empresaprox.html', {'empresas': empresas, 'name':'empresaprox'})


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
    roiSolar = None

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
            roiSolar = (economia_anual / custo_instalacao) * 100
        else:
            roiSolar = 0

    return render(request, 'informacaosolar.html', {'name': 'Informação Solar', 'roi': roiSolar})

def faq(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request,"faq.html",{'form':form})

def add_empresas(request):
    if request.method == "POST":
        form =  EmpresasProxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/empresaprox')
    else:
        form = EmpresasProxForm()
        return render(request, 'add_empresas.html', {'form': form})

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


def simulador(request):
    return render(request, 'simulador.html', context={
        'name': 'Simulador Solar'
    })


@csrf_exempt
def resultados(request):
    if request.method == 'POST':
        form = RoiForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            print('Formulário inválido:', form.errors)
    else:
        form = RoiForm()
    return render(request, 'resultados.html', {'name': 'Resultados do Simulador', 'form': form})
