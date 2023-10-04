from django.urls import path
from Budget.views import *

urlpatterns = [
    path('orcamento/', orcamento, name='orcamento'),  # Orçamento
    path('', home,name=''),  # Área Disponível
    path('calculadora/', calculadora,name='calculadora'),  # Calculadora Solar
    path('suporte/', suporte,name='suporte'),  # Contato
    path('informacoes/', informacoes,name='informacoes'),  # Informações
    path('sobrenos/', sobreNos,name='sobrenos'),  # Sobre Nós
    path('empresas/', empresas,name='empresas'),  # Empresas Próximas A Mim
    path('potencial/', potencial,name='potencial'),  # Potencial de Geração de Energia
    path('area/',area,name='area')
]
