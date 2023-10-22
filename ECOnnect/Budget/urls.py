from Budget.views import (area, calculadora, empresas, informacoes, orcamento,
                          potencial, sobreNos, suporte)
from django.urls import path

from . import views

urlpatterns = [
    path('orcamento', views.orcamento, name='orcamento'),  # Orçamento
    path('', views.area, name='area'),  # Área Disponível
    path('calculadora', views.calculadora, name='calculadora'),  # Calculadora Solar
    path('suporte', views.suporte, name='suporte'),  # Contato
    path('informacoes', views.informacoes, name='informacoes'),  # Informações
    path('sobreNos', views.sobreNos, name='sobreNos'),  # Sobre Nós
    path('empresas', views.empresas, name='empresas'),  # Empresas Próximas A Mim
    path('potencial', views.potencial, name='potencial'),  # Potencial de Geração de Energia
]
