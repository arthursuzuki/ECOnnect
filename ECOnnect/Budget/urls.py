from django.urls import path
from Budget.views import orcamento, suporte, calculadora, informacoes
from Budget.views import sobreNos, empresas, area, potencial

urlpatterns = [
    path('orcamento/', orcamento),  # Orçamento
    path('area/', area),  # Área Disponível
    path('calculadora/', calculadora),  # Calculadora Solar
    path('suporte/', suporte),  # Contato
    path('informacoes/', informacoes),  # Informações
    path('sobreNos/', sobreNos),  # Sobre Nós
    path('empresas/', empresas),  # Empresas Próximas A Mim
    path('potencial/', potencial),  # Potencial de Geração de Energia
]
