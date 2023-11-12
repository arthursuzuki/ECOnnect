from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import login as auth_login

from .forms import ContatoForm, PerfilForm, CreditoCarb


# Create your views here.
def orcamento(request):
    return render(request, 'global/orcamento.html', context={
        'name': 'Cálculo Orçamento'
    })

def home(request):
    return render(request, 'global/home.html', context={
        'name': 'ECONNECT'
    })

def empresaprox(request):
    return render(request, 'global/empresaprox.html', context={
        'name': 'Empresa próxima'
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

'''def infocredito(request):
    return render(request, 'global/infocredito.html', context={
        'name': 'Créditos de Carbono'
    })'''

def infocredito(request):
    # Supondo que o usuário esteja autenticado
    if request.user.is_authenticated:
        # Recupere os créditos de carbono associados ao usuário
        creditos_carbono = CreditoCarb.objects.filter(user=request.user)
        return render(request, 'global/infocredito.html', context={
            'name': 'Créditos de Carbono',
            'creditos_carbono': creditos_carbono
        })
    else:
        return render(request, 'global/infocredito.html', context={
            'name': 'Créditos de Carbono',
            'creditos_carbono': None  # Ou qualquer valor padrão que você deseje
        }) 

def login(request):
    return render(request, 'global/login.html', context={
        'name': 'Login'
    })

def cadastro(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PerfilForm(request.POST)
    return render(request, 'global/cadastro.html',{'form':form ,'name':'Cadastro'})

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



# Teste infocredito

def calcular_creditos(request):
    if request.method == 'POST' and request.user.is_authenticated:
        eletricidade = float(request.POST.get('eletricidade', 0))
        credito_calculado = eletricidade * 0.7
        # Atualize o banco de dados com os créditos calculados
        usuario = request.user
        credito_carbono, created = CreditoCarb.objects.get_or_create(user=usuario)
        credito_carbono.valor += credito_calculado
        credito_carbono.save()
        return JsonResponse({'success': True, 'credito_calculado': credito_calculado})
    return JsonResponse({'success': False, 'message': 'Requisição inválida'})


def loginPage(request):
    if request.method == "POST":
        try:
            print(request.POST.get("email"))
            username = UserController.existe(email=request.POST.get("email")).username
            user = authenticate(request, username=username, password=request.POST.get("password"))

            if (user):
                login(request, user)

            return redirect("/")
        except Exception as e:
            print(e)
            return redirect("/login?error=1")
    else:
        context = {"error": request.GET.get("error", 0)}
        return render(request, 'auth/login.html', context)