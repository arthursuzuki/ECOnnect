from Budget.views import (area, calculadora, empresaprox, feedback,
                          informacaosolar, orcamento, potencial, sobreNos,
                          suporte)
from django.urls import path

from . import views

urlpatterns = [
    path('orcamento', views.orcamento, name='orcamento'),  # Orçamento
    path('faq', views.faq, name='faq'),  # Fale conosco
    path('login', views.login, name='login'),  # Login
    path('cadastro', views.cadastro, name='cadastro'),  # Cadastro
    path('area/', views.area, name='area'),  # Área Disponível
    path('infocredito', views.infocredito, name='infocredito'),  # Créditos de Carbono
    path('', views.home, name='home'),  # Home
    path('calculadora', views.calculadora, name='calculadora'),  # Calculadora Solar
    path('suporte', views.suporte, name='suporte'),  # Contato
    path('informacoes', views.informacaosolar, name='informacoes'),  # Informações
    path('sobreNos', views.sobreNos, name='sobreNos'),  # Sobre Nós
    path('empresaprox', views.empresaprox, name='empresaprox'),  # Empresas Próximas A Mim
    path('potencial', views.potencial, name='potencial'),  # Potencial de Geração de Energia
    path('informacaosolar', views.informacaosolar, name='informacaosolar'),  # Informação Solar
    path('feedback/', views.feedback,name='feedback'), #Feedbacks
    path('simulador', views.simulador, name='simulador'),  # Simuladr
    path('resultados', views.resultados, name='resultados'),  # Resultados
    path('add_empresas', views.add_empresas, name='add_empresas')  # Adicionar Empresas ###Novo
]
