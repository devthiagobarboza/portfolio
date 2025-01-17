from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import ClientesForm, AnamneseForm, EnderecoFormSet, get_endereco_formset, SessaoClinicaForm
from .models import Clientes, Endereco

# Create your views here.

CLIENTES = 'conectapsiApp/clientes.html'
CADASTRAR_CLIENTE = 'conectapsiApp/cadastroclientes.html'
LISTAR_CLIENTES = 'conectapsiApp/listarclientes.html'
HOME = 'conectapsiApp/base.html'
ANAMNESE = 'conectapsiApp/anamnese.html'
SESSAO_CLINICA = 'conectapsiApp/sessaoclinica.html'
DOCUMENTOS = 'conectapsiApp/documentos.html'


def home(request):
    return render(request, HOME)


def clientes_form_base(request):
    return render(request, CADASTRAR_CLIENTE, {'clientes_form': ClientesForm(), 'endereco_formset': EnderecoFormSet()})


def evolucao(request):
    return HttpResponse('<h1>Evolução Paciente</h1>')


def clientes(request):
    return render(request, CLIENTES)


def cadastrar_clientes(request):
    endereco_formset = EnderecoFormSet()
    try:
        if request.method == 'POST':
            clientes_form = ClientesForm(request.POST)
            endereco_formset = EnderecoFormSet(request.POST)

            if clientes_form.is_valid() and endereco_formset.is_valid():
                cliente = clientes_form.save()
                enderecos = endereco_formset.save(commit=False)
                for endereco in enderecos:
                    endereco.id_pct = cliente
                    endereco.save()

                msg = 'Cliente cadastrado com sucesso'
            else:
                msg = clientes_form.errors and endereco_formset.errors

            return render(request, CADASTRAR_CLIENTE, {'clientes_form': ClientesForm(),
                                                       'endereco_formset': EnderecoFormSet(),
                                                       'msg': msg})
    except Exception as ex:
        msg = ex.args
        return render(request, CADASTRAR_CLIENTE, {'clientes_form': ClientesForm(),
                                                   'endereco_formset': EnderecoFormSet(),
                                                   'msg': msg})


def listar_clientes(request):
    clientes = Clientes.objects.all()
    form = ClientesForm()
    campos = clientes.first().__dict__.keys() if clientes.exists() else []
    return render(request, LISTAR_CLIENTES, {'clientes': clientes, 'campos': campos, 'form': form})


def alterar_cliente(request, codigo):
    try:
        # Obtenha o cliente pelo ID
        cliente = get_object_or_404(Clientes, pk=codigo)
        EnderecoFormSet = get_endereco_formset(extra=0, can_delete=False)

        # Se o método for POST, salve as alterações
        if request.method == 'POST':
            clientes_form = ClientesForm(request.POST, instance=cliente)  # Formulário vinculado ao cliente
            endereco_formset = EnderecoFormSet(request.POST, instance=cliente)

            if clientes_form.is_valid() and endereco_formset.is_valid():
                # Salve o cliente e os endereços
                cliente = clientes_form.save()
                enderecos = endereco_formset.save(commit=False)
                for endereco in enderecos:
                    endereco.id_pct = cliente  # Relacione os endereços ao cliente
                    endereco.save()

                msg = 'Cliente alterado com sucesso'
                return redirect('conectapsiApp:listarclientes')  # Redirecione após salvar
            else:
                msg = clientes_form.errors and endereco_formset.errors
        else:
            # Carregue os formulários com os dados existentes
            clientes_form = ClientesForm(instance=cliente)
            endereco_formset = EnderecoFormSet(instance=cliente)

            msg = None  # Não há mensagem em GET

        # Renderize o template com os formulários e a mensagem
        return render(request, 'conectapsiApp/alterarcliente.html', {
            'clientes_form': clientes_form,
            'endereco_formset': endereco_formset,
            'msg': msg
        })

    except Exception as ex:
        msg = ex.args
        return render(request, 'conectapsiApp/alterarcliente.html', {
            'clientes_form': ClientesForm(instance=cliente),
            'endereco_formset': EnderecoFormSet(instance=cliente),
            'msg': msg
        })


def excluir_cliente(request, codigo):
    clientes = Clientes.objects.all()
    try:
        cliente = Clientes.objects.get(pk=codigo)
        cliente_excluido = cliente.delete()

        if cliente_excluido[0] > 0:
            msg = 'Cliente excluído com sucesso.'
        else:
            msg = 'Cliente não encontrado.'

        return render(request, LISTAR_CLIENTES, {'clientes': clientes, 'msg': msg})

    except Exception as ex:
        msg = ex.args
        return render(request, LISTAR_CLIENTES, {'clientes': clientes, 'msg': msg})


def anamnese_form_base(request):
    form = AnamneseForm()
    return render(request, ANAMNESE, {'form': form})


def cadastrar_anamnese(request):
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form.save()

            msg = 'Anamnese Salva Com Sucesso!'
        else:
            msg = 'Erro ao Criar Anamnese'
        return render(request, ANAMNESE, {'form': form, 'msg': msg})


def sessao_clinica_base(request):
    form = SessaoClinicaForm()
    return render(request, SESSAO_CLINICA, {'form': form})


def cadastrar_sessao_clinica(request):
    if request.method == 'POST':
        form = SessaoClinicaForm(request.POST)
        if form.is_valid():
            form.save()

            msg = 'Sessão Clínica Salva com Sucesso!'
        else:
            msg = 'Erro ao Salvar Sessão Clínica!'
        return render(request, SESSAO_CLINICA, {'form': form, 'msg': msg})


def documentos(request):
    return render(request, DOCUMENTOS)
