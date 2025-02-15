from django.urls import path
from . import views

app_name = 'conectapsiApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('Clientes/', views.clientes, name='clientes'),
    path('CadastroClientes/', views.clientes_form_base, name='cadastroclientes'),
    path('Evolucao/', views.evolucao, name='evolucao'),
    path('CadastrarClientes/', views.cadastrar_clientes, name='cadastrarclientes'),
    path('Clientes/ConsultarClientes/', views.listar_clientes, name='listarclientes'),
    path('Clientes/Excluir/<int:codigo>', views.excluir_cliente, name='excluircliente'),
    path('Clientes/Alterar/<int:codigo>', views.alterar_cliente, name='alterarcliente'),

    path('Clientes/Anamnese/', views.anamnese_form_base, name='anamnese'),
    path('Clientes/Anamnese/Consultar/', views.listar_anamense, name='listaranamnese'),
    path('Clientes/Anamnese/Cadastrar/', views.cadastrar_anamnese, name='cadastraranamnese'),
    path('Clientes/Anamnese/Alterar/<int:codigo>', views.alterar_anamnese, name='alteraranamnese'),
    path('Clientes/Anamnese/Excluir/<int:codigo>', views.excluir_anamnese, name='excluiranamnese'),
    path('SessaoClinica/', views.sessao_clinica_base, name='sessaoclinica'),
    path('CadastrarSessaoClinica/', views.cadastrar_sessao_clinica, name='cadastrarsessaoclinica'),

    #Sessão documentos
    path('Documentos/', views.documentos, name='documentos'),

    # Gerar Anamnese
    path('Documentos/GerarAnamnese/<int:codigo>', views.gerar_relatorio_anamnese, name='gerar_anamnese')
]
