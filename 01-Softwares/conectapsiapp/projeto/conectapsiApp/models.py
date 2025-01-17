# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
import re


def validar_cpf(value):
    cpf = re.sub(r'\D', '', value)  # Remove caracteres não numéricos

    if not cpf or len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    # Validação dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * (i + 1 - num) for num in range(0, i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            raise ValidationError("CPF inválido.")

    return value


class Endereco(models.Model):
    id_end = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    uf = models.CharField(max_length=2, null=False)
    cep = models.CharField(max_length=8, null=False)
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE, related_name='enderecos')

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_end,
                                                           self.rua,
                                                           self.numero,
                                                           self.complemento,
                                                           self.bairro,
                                                           self.cidade,
                                                           self.uf,
                                                           self.cep,
                                                           self.id_pct)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_end,
                                                           self.rua,
                                                           self.numero,
                                                           self.complemento,
                                                           self.bairro,
                                                           self.cidade,
                                                           self.uf,
                                                           self.cep,
                                                           self.id_pct)

    objects = models.Manager()


class Clientes(models.Model):
    id_pct = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    sobrenome = models.CharField(max_length=100, null=False, default="")
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=20, null=False)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=14, null=False, validators=[validar_cpf])
    estado_civil = models.CharField(max_length=10, null=False)
    conjuge_nome = models.CharField(max_length=100, blank=True, null=True)
    conjuge_idade = models.CharField(max_length=10, blank=True, null=True)
    conjuge_sexo = models.CharField(max_length=10, blank=True, null=True)
    filhos_nome = models.CharField(max_length=100, blank=True, null=True)
    filhos_idade = models.CharField(max_length=10, blank=True, null=True)
    filhos_sexo = models.CharField(max_length=10, blank=True, null=True)
    religiao = models.CharField(max_length=25, blank=True, null=True)
    escolaridade = models.CharField(max_length=20, blank=True, null=True)
    profissao = models.CharField(max_length=20, blank=True, null=True)
    telefone_principal = models.CharField(max_length=15, null=False)
    telefone_emergencia = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, null=False)
    observacoes = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Anamnese(models.Model):
    id_anamense = models.AutoField(primary_key=True)
    tipo_de_atendimento = models.CharField(max_length=50, blank=True, null=True)
    plano_de_saude = models.CharField(max_length=50, blank=True, null=True)
    numero_carteirinha = models.CharField(max_length=50, blank=True, null=True)
    historico_medico = models.TextField(blank=True, null=True)
    historico_familiar = models.TextField(blank=True, null=True)
    diagnosticos_preexistentes = models.TextField(blank=True, null=True)
    uso_medicamentos = models.TextField(blank=True, null=True)
    uso_medicamentos_alternativos = models.TextField(blank=True, null=True)
    uso_de_drogas = models.TextField(blank=True, null=True)
    conceituacao_psicologica_do_caso = models.TextField(blank=True, null=True)
    queixa_principal = models.TextField(blank=True, null=True)
    possibilidade_de_horarios = models.TextField(blank=True, null=True)
    fez_terapia_anterior = models.CharField(max_length=3, blank=True, null=True)
    quando_fez_terapia_anterior = models.CharField(max_length=15, blank=True, null=True)
    expectativa_e_objetivo_do_paciente = models.TextField(blank=True, null=True)
    sintomas_apresentados = models.TextField(blank=True, null=True)
    transtornos_psiquiatricos_anteriores = models.TextField(blank=True, null=True)
    transtornos_psiquiatricos_familiares = models.TextField(blank=True, null=True)
    doenca_importante_que_teve = models.TextField(blank=True, null=True)
    aplicacao_de_teste = models.TextField(blank=True, null=True)
    historico_da_queixa_quando_se_iniciou = models.TextField(blank=True, null=True)
    eventos_traumaticos_da_vida = models.TextField(blank=True, null=True)
    eventos_que_agravam_a_crise = models.TextField(blank=True, null=True)
    tentativa_de_suicidio = models.TextField(blank=True, null=True)
    relacionamentos_importantes_mae = models.TextField(blank=True, null=True)
    relacionamentos_importantes_pai = models.TextField(blank=True, null=True)
    relacionamentos_importantes_irmaos = models.TextField(blank=True, null=True)
    relacionamentos_importantes_filhos = models.TextField(blank=True, null=True)
    relacionamentos_importantes_outros = models.TextField(blank=True, null=True)
    observacao_sobre_dinamica_familiar_atual = models.TextField(blank=True, null=True)
    infancia_gravidez_planejada = models.TextField(blank=True, null=True)
    infancia_amamentacao = models.TextField(blank=True, null=True)
    infancia_estressores_crises = models.TextField(blank=True, null=True)
    infancia_transtornos_infantis = models.TextField(blank=True, null=True)
    infancia_comentarios = models.TextField(blank=True, null=True)
    adolescencia_experiencias_afetivas_marcantes = models.TextField(blank=True, null=True)
    adolescencia_experiencias_sexuais_marcantes = models.TextField(blank=True, null=True)
    adolescencia_independencia = models.TextField(blank=True, null=True)
    adolescencia_circulo_de_amizades = models.TextField(blank=True, null=True)
    vida_adulta_relacionamento_com_parceiro = models.TextField(blank=True, null=True)
    vida_adulta_vida_sexual_atual = models.TextField(blank=True, null=True)
    vida_adulta_situacao_financeira = models.TextField(blank=True, null=True)
    vida_adulta_abordo_espontaneo = models.TextField(blank=True, null=True)
    vida_adulta_apoio_social = models.TextField(blank=True, null=True)
    vida_adulta_outros_transtornos = models.TextField(blank=True, null=True)
    vida_adulta_principais_lazeres = models.TextField(blank=True, null=True)
    observacao_e_linguagem_nao_verbal = models.TextField(blank=True, null=True)
    atendimentos_prestados_profissional = models.CharField(max_length=100, blank=True, null=True)
    atendimentos_prestados_encaminhamentos = models.CharField(max_length=100, blank=True, null=True)
    atendimentos_prestados_terapeutica_utilizada = models.CharField(max_length=255, blank=True, null=True)
    atendimentos_prestados_destino_do_caso_alta = models.CharField(max_length=4, blank=True, null=True)
    atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao = models.CharField(max_length=100,
                                                                                               blank=True, null=True)
    atendimentos_prestados_destino_do_caso_abandono = models.CharField(max_length=255, blank=True, null=True)
    atendimentos_prestados_destino_do_caso_outro_profissional = models.CharField(max_length=100, blank=True, null=True)
    atendimentos_prestados_destino_do_caso_interrompido = models.CharField(max_length=255, blank=True, null=True)
    atendimentos_prestados_destino_do_caso_melhoras_obtidas = models.TextField(blank=True, null=True)
    atendimentos_prestados_destino_do_caso_outras_obs = models.TextField(blank=True, null=True)
    id_pct = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return ('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}').format(
            self.id_pct,
            self.id_anamense,
            self.tipo_de_atendimento,
            self.plano_de_saude,
            self.numero_carteirinha,
            self.historico_medico,
            self.historico_familiar,
            self.diagnosticos_preexistentes,
            self.uso_medicamentos,
            self.uso_medicamentos_alternativos,
            self.uso_de_drogas,
            self.conceituacao_psicologica_do_caso,
            self.queixa_principal,
            self.possibilidade_de_horarios,
            self.fez_terapia_anterior,
            self.quando_fez_terapia_anterior,
            self.expectativa_e_objetivo_do_paciente,
            self.sintomas_apresentados,
            self.transtornos_psiquiatricos_anteriores,
            self.transtornos_psiquiatricos_familiares,
            self.doenca_importante_que_teve,
            self.aplicacao_de_teste,
            self.historico_da_queixa_quando_se_iniciou,
            self.eventos_traumaticos_da_vida,
            self.eventos_que_agravam_a_crise,
            self.tentativa_de_suicidio,
            self.relacionamentos_importantes_mae,
            self.relacionamentos_importantes_pai,
            self.relacionamentos_importantes_irmaos,
            self.relacionamentos_importantes_filhos,
            self.relacionamentos_importantes_outros,
            self.observacao_sobre_dinamica_familiar_atual,
            self.infancia_gravidez_planejada,
            self.infancia_amamentacao,
            self.infancia_estressores_crises,
            self.infancia_transtornos_infantis,
            self.infancia_comentarios,
            self.adolescencia_experiencias_afetivas_marcantes,
            self.adolescencia_experiencias_sexuais_marcantes,
            self.adolescencia_independencia,
            self.adolescencia_circulo_de_amizades,
            self.vida_adulta_relacionamento_com_parceiro,
            self.vida_adulta_vida_sexual_atual,
            self.vida_adulta_situacao_financeira,
            self.vida_adulta_abordo_espontaneo,
            self.vida_adulta_apoio_social,
            self.vida_adulta_outros_transtornos,
            self.vida_adulta_principais_lazeres,
            self.observacao_e_linguagem_nao_verbal,
            self.atendimentos_prestados_profissional,
            self.atendimentos_prestados_encaminhamentos,
            self.atendimentos_prestados_terapeutica_utilizada,
            self.atendimentos_prestados_destino_do_caso_alta,
            self.atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao,
            self.atendimentos_prestados_destino_do_caso_abandono,
            self.atendimentos_prestados_destino_do_caso_outro_profissional,
            self.atendimentos_prestados_destino_do_caso_interrompido,
            self.atendimentos_prestados_destino_do_caso_melhoras_obtidas,
            self.atendimentos_prestados_destino_do_caso_outras_obs
        )

    def __repr__(self):
        return ('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '
                '{}, {}, {}, {}, {}, {}').format(
            self.id_pct.name,
            self.id_anamense,
            self.tipo_de_atendimento,
            self.plano_de_saude,
            self.numero_carteirinha,
            self.historico_medico,
            self.historico_familiar,
            self.diagnosticos_preexistentes,
            self.uso_medicamentos,
            self.uso_medicamentos_alternativos,
            self.uso_de_drogas,
            self.conceituacao_psicologica_do_caso,
            self.queixa_principal,
            self.possibilidade_de_horarios,
            self.fez_terapia_anterior,
            self.quando_fez_terapia_anterior,
            self.expectativa_e_objetivo_do_paciente,
            self.sintomas_apresentados,
            self.transtornos_psiquiatricos_anteriores,
            self.transtornos_psiquiatricos_familiares,
            self.doenca_importante_que_teve,
            self.aplicacao_de_teste,
            self.historico_da_queixa_quando_se_iniciou,
            self.eventos_traumaticos_da_vida,
            self.eventos_que_agravam_a_crise,
            self.tentativa_de_suicidio,
            self.relacionamentos_importantes_mae,
            self.relacionamentos_importantes_pai,
            self.relacionamentos_importantes_irmaos,
            self.relacionamentos_importantes_filhos,
            self.relacionamentos_importantes_outros,
            self.observacao_sobre_dinamica_familiar_atual,
            self.infancia_gravidez_planejada,
            self.infancia_amamentacao,
            self.infancia_estressores_crises,
            self.infancia_transtornos_infantis,
            self.infancia_comentarios,
            self.adolescencia_experiencias_afetivas_marcantes,
            self.adolescencia_experiencias_sexuais_marcantes,
            self.adolescencia_independencia,
            self.adolescencia_circulo_de_amizades,
            self.vida_adulta_relacionamento_com_parceiro,
            self.vida_adulta_vida_sexual_atual,
            self.vida_adulta_situacao_financeira,
            self.vida_adulta_abordo_espontaneo,
            self.vida_adulta_apoio_social,
            self.vida_adulta_outros_transtornos,
            self.vida_adulta_principais_lazeres,
            self.observacao_e_linguagem_nao_verbal,
            self.atendimentos_prestados_profissional,
            self.atendimentos_prestados_encaminhamentos,
            self.atendimentos_prestados_terapeutica_utilizada,
            self.atendimentos_prestados_destino_do_caso_alta,
            self.atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao,
            self.atendimentos_prestados_destino_do_caso_abandono,
            self.atendimentos_prestados_destino_do_caso_outro_profissional,
            self.atendimentos_prestados_destino_do_caso_interrompido,
            self.atendimentos_prestados_destino_do_caso_melhoras_obtidas,
            self.atendimentos_prestados_destino_do_caso_outras_obs
        )


class SessaoClinica(models.Model):
    id_sc = models.AutoField(primary_key=True)
    objetivos = models.TextField(blank=True, null=True)
    data_atendimento = models.DateField(default='')
    numero_da_sessao = models.IntegerField(blank=True, null=True)
    pontos_importantes_da_sessao = models.TextField(blank=True, null=True)
    principais_sintomas = models.TextField(blank=True, null=True)
    observacoes_clinicas = models.TextField(blank=True, null=True)
    evolucao = models.TextField(blank=True, null=True)
    id_pct = models.ForeignKey('Clientes', on_delete=models.CASCADE, related_name='nome_cliente')

    def __str__(self):
        return self.id_pct.name


class Consultas(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    hora = models.TimeField()
    data = models.DateField()
    forma_pagamento = models.CharField(max_length=20, blank=True, null=True)
    responsavel_financeiro = models.CharField(max_length=100, blank=True, null=True)
    observacoes_gerais = models.TextField(blank=True, null=True)
    valor_pagamento = models.FloatField(blank=True, null=True)
    faltas = models.CharField(max_length=3, null=False)
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.id_consulta,
                                                   self.hora,
                                                   self.data,
                                                   self.forma_pagamento,
                                                   self.responsavel_financeiro,
                                                   self.observacoes_gerais,
                                                   self.faltas)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.id_consulta,
                                                   self.hora,
                                                   self.data,
                                                   self.forma_pagamento,
                                                   self.responsavel_financeiro,
                                                   self.observacoes_gerais,
                                                   self.faltas)


class uploadFile(models.Model):
    id_upfile = models.AutoField(primary_key=True)
    arquivo = models.FileField(upload_to='uploads/')
    nome_do_arquivo = models.CharField(max_length=255)
    data_upload = models.DateTimeField(auto_now_add=True)
    tamanho_do_arquivo = models.IntegerField()
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.id_upfile,
                                           self.arquivo,
                                           self.nome_do_arquivo,
                                           self.data_upload,
                                           self.tamanho_do_arquivo)

    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(self.id_upfile,
                                           self.arquivo,
                                           self.nome_do_arquivo,
                                           self.data_upload,
                                           self.tamanho_do_arquivo)
