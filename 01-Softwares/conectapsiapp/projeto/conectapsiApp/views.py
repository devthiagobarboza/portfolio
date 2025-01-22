from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import ClientesForm, AnamneseForm, EnderecoFormSet, get_endereco_formset, SessaoClinicaForm
from .models import Clientes, Anamnese

# Create your views here.

CLIENTES = 'conectapsiApp/clientes.html'
CADASTRAR_CLIENTE = 'conectapsiApp/cadastroclientes.html'
LISTAR_CLIENTES = 'conectapsiApp/listarclientes.html'
HOME = 'conectapsiApp/base.html'
ANAMNESE = 'conectapsiApp/anamnese.html'
LISTAR_ANAMNESE = 'conectapsiApp/listaranamnese.html'
ALTERAR_ANAMNESE = 'conectapsiApp/alteraranamnese.html'
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
    return render(request, LISTAR_CLIENTES, {'clientes': clientes, 'form': form})


def alterar_cliente(request, codigo):
    global EnderecoFormSet
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

        # Renderize o template com os formulários e a mensagem
        return render(request, 'conectapsiApp/alterarcliente.html', {
            'clientes_form': clientes_form,
            'endereco_formset': endereco_formset,
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
            print('Anamnese Salva Com Sucesso!')
            return redirect('conectapsiApp:anamnese')

        else:
            msg = 'Erro ao Criar Anamnese'
        return render(request, ANAMNESE, {'form': form, 'msg': msg})


def listar_anamense(request):
    clientes = Clientes.objects.all()
    anamneses = Anamnese.objects.all()
    cliente_form = ClientesForm()
    anamnese_form = AnamneseForm()
    return render(request, LISTAR_ANAMNESE, {'anamneses': anamneses, 'clientes': clientes,
                                             'cliente_form': cliente_form,
                                             'anamnese_form': anamnese_form})


def alterar_anamnese(request, codigo):
    anamnese = get_object_or_404(Anamnese, pk=codigo)
    cliente = anamnese.id_pct

    try:
        if request.method == 'POST':
            anamnese_form = AnamneseForm(request.POST, instance=anamnese)
            clientes_form = ClientesForm(request.POST, instance=cliente)

            if anamnese_form.is_valid():
                anamnese = anamnese_form.save()
                msg = 'Anamnese alterada com sucesso.'
                print(msg)
                return redirect('conectapsiApp:listaranamnese')

            else:
                msg = anamnese_form.errors and clientes_form.errors
        else:
            anamnese_form = AnamneseForm(instance=anamnese)
            clientes_form = ClientesForm(instance=cliente)

        return render(request, 'conectapsiApp/alteraranamnese.html', {
            'anamnese_form': anamnese_form,
            'clientes_form': clientes_form})

    except Exception as ex:
        msg = ex.args
        return render(request, 'conectapsiApp/alteraranamnese.html', {
            'anamnese_form': AnamneseForm(instance=anamnese),
            'msg': msg})


def excluir_anamnese(request, codigo):
    anamnese = Anamnese.objects.all()
    try:
        anamnese = Anamnese.objects.get(pk=codigo)
        anamnese_excluida = anamnese.delete()

        if anamnese_excluida[0] > 0:
            msg = 'Cliente excluído com sucesso.'
        else:
            msg = 'Cliente não encontrado.'
        return redirect('conectapsiApp:listaranamnese')
    except Exception as ex:
        msg = ex.args
        return redirect('conectapsiApp:listaranamnese')


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
