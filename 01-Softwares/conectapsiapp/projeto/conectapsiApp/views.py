from io import BytesIO
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from docx import Document
import os
from .forms import ClientesForm, AnamneseForm, EnderecoFormSet, get_endereco_formset, SessaoClinicaForm
from .models import Clientes, Anamnese, Endereco

# Create your views here.

CLIENTES = 'conectapsiApp/clientes.html'
CADASTRAR_CLIENTE = 'conectapsiApp/cadastroclientes.html'
LISTAR_CLIENTES = 'conectapsiApp/listarclientes.html'
HOME = 'conectapsiApp/base.html'
ANAMNESE = 'conectapsiApp/anamnese.html'
LISTAR_ANAMNESE = 'conectapsiApp/listaranamnese.html'
ALTERAR_ANAMNESE = 'conectapsiApp/alteraranamnese.html'
SESSAO_CLINICA = 'conectapsiApp/sessaoclinica.html'
DOCUMENTOS = 'conectapsiApp/templates/documentos'


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
                print('Cliente cadastrado com sucesso.')

            else:
                print('Erro no formulario', clientes_form.errors)
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
    cliente = get_object_or_404(Clientes, pk=codigo)
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


def gerar_relatorio_anamnese(request, codigo):
    cliente = get_object_or_404(Clientes, pk=codigo)
    anamnese = Anamnese.objects.filter(id_pct=cliente).first()
    endereco = Endereco.objects.filter(id_pct=cliente).first()

    if not anamnese:
        return HttpResponse("Anamnese não encontrada.", status=404)

    if not endereco:
        return HttpResponse("Endereço não encontrado", status=404)

    # Definir o endereço para buscar o modelo do documento
    modelo_anamnese_path = os.path.join('conectapsiApp', 'templates', 'documentos', 'anamnese_adulto.docx')

    # carregar o documento
    doc = Document(modelo_anamnese_path)

    # Dados que serão substituidos
    dados = {

        "{{NOME}}": cliente.nome,
        "{{SOBRENOME}}": cliente.sobrenome,
        "{{GENERO}}": cliente.genero,
        "{{DTNASC}}": str(cliente.data_nascimento),
        "{{ESTADO_CIVIL}}": cliente.estado_civil,
        "{{RUA}}": endereco.rua,
        "{{NUMERO}}": endereco.numero,
        "{{BAIRRO}}": endereco.bairro,
        "{{CIDADE}}": endereco.cidade,
        "{{UF}}": endereco.uf,
        "{{PROFISSAO}}": cliente.profissao,
        "{{ESCOLARIDADE}}": cliente.escolaridade,
        "{{RELIGIAO}}": cliente.religiao,
        "{{TEL}}": cliente.telefone_principal,
        "{{TEL_EMER}}": cliente.telefone_emergencia,
        "{{FILHOS}}": cliente.filhos_nome,
        "{{FILHOS_IDADE}}": cliente.filhos_idade,
        "{{FILHOS_SEXO}}": cliente.filhos_sexo,
        "{{CONJUGE}}": cliente.conjuge_nome,
        "{{CONJUGE_IDADE}}": cliente.conjuge_idade,
        "{{CONJUGE_PROFISSAO}}": cliente.conjuge_idade,
        "{{QX_PRINCIPAL}}": anamnese.queixa_principal,
        "{{POSSIBILIDADE_HORARIO}}": anamnese.possibilidade_de_horarios,
        "{{FEZ_TERAPIA}}": anamnese.fez_terapia_anterior,
        "{{EXPECTATIVAS}}": anamnese.expectativa_e_objetivo_do_paciente,
        "{{SINTOMAS_APRESENTADOS}}": anamnese.sintomas_apresentados,
        "{{CONCEITUACAO}}": anamnese.conceituacao_psicologica_do_caso,
        "{{TRANSTORNO_ANTERIORES}}": anamnese.transtornos_psiquiatricos_anteriores,
        "{{TRANSTORNO_FAMILIAR}}": anamnese.transtornos_psiquiatricos_familiares,
        "{{DOENCAS_QUE_TEVE}}": anamnese.doenca_importante_que_teve,
        "{{MEDICACAO_TOMANDO}}": anamnese.uso_medicamentos,
        "{{MEDICACAO_ALTERNATIVA}}": anamnese.uso_medicamentos_alternativos,
        "{{TESTES}}": anamnese.aplicacao_de_teste,
        "{{HISTORICO}}": anamnese.historico_da_queixa_quando_se_iniciou,
        "{{TRAUMAS}}": anamnese.eventos_traumaticos_da_vida,
        "{{FATORES_TRAUMATICOS}}": anamnese.eventos_que_agravam_a_crise,
        "{{DROGAS}}": anamnese.uso_de_drogas,
        "{{SUICIDIO}}": anamnese.tentativa_de_suicidio,
        "{{REL_MAE}}": anamnese.relacionamentos_importantes_mae,
        "{{REL_PAI}}": anamnese.relacionamentos_importantes_pai,
        "{{REL_IRMAOS}}": anamnese.relacionamentos_importantes_irmaos,
        "{{REL_FILHOS}}": anamnese.relacionamentos_importantes_filhos,
        "{{REL_OUTROS}}": anamnese.relacionamentos_importantes_outros,
        "{{REL_OBS}}": anamnese.relacionamentos_importantes_outros,
        "{{GRAVIDEZ}}": anamnese.infancia_gravidez_planejada,
        "{{AMAMENTACAO}}": anamnese.infancia_amamentacao,
        "{{ESTRESSORES}}": anamnese.infancia_estressores_crises,
        "{{OUTROS_TRANSTORNOS}}": anamnese.infancia_transtornos_infantis,
        "{{COMENTARIOS}}": anamnese.infancia_comentarios,
        "{{ADOL_AFETIVA}}": anamnese.adolescencia_experiencias_afetivas_marcantes,
        "{{ADOL_SEXUAIS}}": anamnese.adolescencia_experiencias_sexuais_marcantes,
        "{{ADOL_INDEPEN}}": anamnese.adolescencia_independencia,
        "{{ADOL_CIRCULO}}": anamnese.adolescencia_circulo_de_amizades,
        "{{ADULTA_PARCEIRO}}": anamnese.vida_adulta_relacionamento_com_parceiro,
        "{{ADULTA_SEXUAL}}": anamnese.vida_adulta_vida_sexual_atual,
        "{{ADULTA_FINCEIRA}}": anamnese.vida_adulta_situacao_financeira,
        "{{ABORTOS}}": anamnese.vida_adulta_abordo_espontaneo,
        "{{ADULTA_APOIO}}": anamnese.vida_adulta_apoio_social,
        "{{ADULTA_OUTROS_TRANSTORNOS}}": anamnese.vida_adulta_outros_transtornos,
        "{{ADULTA_LAZERES}}": anamnese.vida_adulta_principais_lazeres,
        "{{OBSER_NAO_VERBAL}}": anamnese.observacao_e_linguagem_nao_verbal,
        "{{ATENDIMENTO_PROFISSIONAL}}": anamnese.atendimentos_prestados_profissional,
        "{{ENCAMINHAMENTO_FEITO}}": anamnese.atendimentos_prestados_encaminhamentos,
        "{{TERAPEUTICA_UTILIZADA}}": anamnese.atendimentos_prestados_terapeutica_utilizada,
        "{{ALTA}}": anamnese.atendimentos_prestados_destino_do_caso_alta,
        "{{OUTRA_INSTITUICAO}}": anamnese.atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao,
        "{{ABANDONO}}": anamnese.atendimentos_prestados_destino_do_caso_abandono,
        "{{ENC_OUTRO_PROF}}": anamnese.atendimentos_prestados_destino_do_caso_outro_profissional,
        "{{INTERROMPIDO}}": anamnese.atendimentos_prestados_destino_do_caso_interrompido,
        "{{MELHORIAS}}": anamnese.atendimentos_prestados_destino_do_caso_melhoras_obtidas,
        "{{OBS_IMPORTANTES}}": anamnese.atendimentos_prestados_destino_do_caso_outras_obs,














    }

    # Substituir os {{placeholders}} no documento pelos dados dos clientes
    for p in doc.paragraphs:
        for run in p.runs:
            for placeholder, valor in dados.items():
                if placeholder in run.text:
                    run.text = run.text.replace(placeholder, valor)
        # p.text = p.text.replace('{{NOME}} {{SOBRENOME}}', f"{cliente.nome} {cliente.sobrenome}")
        # p.text = p.text.replace('{{SEXO}}', cliente.genero)

    # Salvar documento em memoria
    conteudo_arquivo = BytesIO()
    doc.save(conteudo_arquivo)
    conteudo_arquivo.seek(0)

    # Gerar resposta
    response = HttpResponse(conteudo_arquivo.getvalue(),
                            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

    response['Content-Disposition'] = f'attachment; filename="Anamnese_{cliente.nome}_{cliente.sobrenome}.docx"'

    return response
