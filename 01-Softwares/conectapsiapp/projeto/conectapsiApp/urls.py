from django.urls import path
from .import views

app_name = 'conectapsiApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastroclientes/', views.clientes_form_base, name='cadastroclientes'),
    path('evolucao/', views.evolucao, name='evolucao'),
    path('CadastrarClientes', views.cadastrar_clientes, name='cadastrarclientes'),
    path('Documentos/Anamnese/', views.anamnese_form_base, name='anamnese'),
    path('Documentos/Anamnese/CadastrarAnamnese', views.cadastrar_anamnese, name='cadastraranamnese'),


    #Sessão documentos
    path('Documentos/', views.documentos, name='documentos'),
    

]
