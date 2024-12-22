from django.urls import path
from .import views

app_name = 'conectapsiApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastroclientes/', views.cadastro_clientes, name='cadastroclientes'),
    path('evolucao/', views.evolucao, name='evolucao'),
    path('CadastrarClientes', views.cadastrar_clientes, name='cadastrarclientes'),

    #Sessão documentos
    path('documentos/', views.documentos, name='documentos'),
    

]
