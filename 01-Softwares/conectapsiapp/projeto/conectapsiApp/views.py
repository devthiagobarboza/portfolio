from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClientesForm, AnamneseForm


# Create your views here.

CADASTRAR_CLIENTE = 'conectapsiApp/cadastroclientes.html'
HOME = 'conectapsiApp/home.html'
ANAMNESE = 'conectapsiApp/anamnese.html'




def home(request):
    return render(request, HOME)


def clientes_form_base(request):
    form = ClientesForm()
    # template = loader.get_template('conectapsiApp/cadastroclientes.html')
    return render(request, 'conectapsiApp/cadastroclientes.html', {'form': form})


def evolucao(request):
    return HttpResponse('<h1>Evolução Paciente</h1>')


# def clientes_form(request):
#     try:
#         if request.method == 'POST':
#             form = ClientesForm(request.POST)
#             if form.is_valid():
#                 cliente = Clientes()
#                 cliente.nome = form.cleaned_data['nome']
#                 cliente.sobrenome = form.cleaned_data['sobrenome']
#                 cliente.nome_social = form.cleaned_data['nome_social']
#                 cliente.genero = form.cleaned_data['genero']
#                 cliente.data_nascimento = form.cleaned_data['data_nascimento']
#                 cliente.cpf = form.cleaned_data['cpf']
#                 cliente.estado_civil = form.cleaned_data['estado_civil']
#                 cliente.profissao = form.cleaned_data['profissao']
#                 cliente.telefone_principal = form.cleaned_data['telefone_principal']
#                 cliente.telefone_emergencia = form.cleaned_data['telefone_emergencia']
#                 cliente.email = form.cleaned_data['email']
#                 cliente.observacoes = form.cleaned_data['observacoes']
#                 cliente.save()
#
#                 msg = "Cliente Cadastrado com Sucesso!"
#             else:
#                 msg = form.errors
#
#             return render(request, CADASTRAR_CLIENTE, {'form': ClientesForm(), 'msg': msg})
#
#         else:
#             raise Exception('MethodEnvioError, use POST para formulários')
#
#     except Exception as ex:
#         msg = ex.args
#         return render(request, CADASTRAR_CLIENTE, {'form': ClientesForm(), 'msg': msg})

def clientes_form(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()

            msg = 'Cliente cadastrado com sucesso'
        else:
            msg = form.errors

        return render(request, CADASTRAR_CLIENTE, {'form': ClientesForm(), 'msg': msg})


def anamnese_form_base(request):
    form = AnamneseForm()
    # template = loader.get_template('conectapsiApp/cadastroclientes.html')
    return render(request, 'conectapsiApp/anamnese.html', {'form': form})

def anamnese_form(request):
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form.cleaned_data.save()
            msg = 'Anamnese Salva Com Sucesso!'
        else:
            msg = 'Erro ao Criar Anamnese'
        return render(request, ANAMNESE, {'form': AnamneseForm(), 'msg': msg})


def documentos(request):
    pass


# return render(request, 'conectapsiApp/cadastroclientes.html', {'form': form})
