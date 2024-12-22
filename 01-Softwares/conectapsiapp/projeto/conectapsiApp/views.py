from django.shortcuts import render
from django.http import HttpResponse
from .forms import cadastra_clientes
from .models import Clientes

# Create your views here.

CADASTRAR_CLIENTE = 'conectapsiApp/cadastroclientes.html'
HOME = 'conectapsiApp/home.html'

def home(request):
    return render(request, HOME)


def cadastro_clientes(request):
    form = cadastra_clientes()
    # template = loader.get_template('conectapsiApp/cadastroclientes.html')
    return render(request, 'conectapsiApp/cadastroclientes.html', {'form': form})


def evolucao(request):
    return HttpResponse('<h1>Evolução Paciente</h1>')


def cadastrar_clientes(request):
    try:
        if request.method == 'POST':
            form = cadastra_clientes(request.POST)
            if form.is_valid():
                cliente = Clientes()
                cliente.nome = form.cleaned_data['nome']
                cliente.sobrenome = form.cleaned_data['sobrenome']
                cliente.nome_social = form.cleaned_data['nome_social']
                cliente.genero = form.cleaned_data['genero']
                cliente.data_nascimento = form.cleaned_data['data_nascimento']
                cliente.cpf = form.cleaned_data['cpf']
                cliente.estado_civil = form.cleaned_data['estado_civil']
                cliente.profissao = form.cleaned_data['profissao']
                cliente.telefone_principal = form.cleaned_data['telefone_principal']
                cliente.telefone_emergencia = form.cleaned_data['telefone_emergencia']
                cliente.email = form.cleaned_data['email']
                cliente.observacoes = form.cleaned_data['observacoes']
                cliente.save()

                msg = "Cliente Cadastrado com Sucesso!"
            else:
                msg = form.errors

            return render(request, CADASTRAR_CLIENTE, {'form': cadastra_clientes(), 'msg': msg})

        else:
            raise Exception('MethodEnvioError, use POST para formulários')

    except Exception as ex:
        msg = ex.args
        return render(request, CADASTRAR_CLIENTE, {'form': cadastra_clientes(), 'msg': msg})


# return render(request, 'conectapsiApp/cadastroclientes.html', {'form': form})
