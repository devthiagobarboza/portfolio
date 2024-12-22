# Create your models here.
from django.db import models


class Clientes(models.Model):
    id_pct = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    sobrenome = models.CharField(max_length=100, null=False, default="")
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=20, null=False)
    data_nascimento = models.DateField(null=False)
    cpf = models.CharField(max_length=14, null=False)
    estado_civil = models.CharField(max_length=10, null=False)
    profissao = models.CharField(max_length=20, blank=True, null=True)
    telefone_principal = models.CharField(max_length=15, null=False)
    telefone_emergencia = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, null=False)
    observacoes = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_pct,
                                                                           self.nome,
                                                                           self.sobrenome,
                                                                           self.nome_social,
                                                                           self.genero,
                                                                           self.data_nascimento,
                                                                           self.cpf,
                                                                           self.estado_civil,
                                                                           self.profissao,
                                                                           self.telefone_principal,
                                                                           self.telefone_emergencia,
                                                                           self.email,
                                                                           self.data_cadastro,
                                                                           self.observacoes)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_pct,
                                                                               self.nome,
                                                                               self.sobrenome,
                                                                               self.nome_social,
                                                                               self.genero,
                                                                               self.data_nascimento,
                                                                               self.cpf,
                                                                               self.estado_civil,
                                                                               self.profissao,
                                                                               self.telefone_principal,
                                                                               self.telefone_emergencia,
                                                                               self.email,
                                                                               self.data_cadastro,
                                                                               self.observacoes)


class Endereco(models.Model):
    id_end = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    uf = models.CharField(max_length=2, null=False)
    cep = models.CharField(max_length=8, null=False)
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

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


class historico_clinico(models.Model):
    id_hc = models.AutoField(primary_key=True)
    tipo_de_atendimento = models.CharField(max_length=50, blank=True, null=True)
    plano_de_saude = models.CharField(max_length=50, blank=True, null=True)
    numero_carteirinha = models.CharField(max_length=50, blank=True, null=True)
    historico_medico = models.TextField(blank=True, null=True)
    historico_familiar = models.TextField(blank=True, null=True)
    diagnosticos_preexistentes = models.TextField(blank=True, null=True)
    uso_medicamentos = models.TextField(blank=True, null=True)
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_hc,
                                                       self.tipo_de_atendimento,
                                                       self.plano_de_saude,
                                                       self.numero_carteirinha,
                                                       self.historico_medico,
                                                       self.historico_familiar,
                                                       self.diagnosticos_preexistentes,
                                                       self.uso_medicamentos,
                                                       self.id_pct)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_hc,
                                                       self.tipo_de_atendimento,
                                                       self.plano_de_saude,
                                                       self.numero_carteirinha,
                                                       self.historico_medico,
                                                       self.historico_familiar,
                                                       self.diagnosticos_preexistentes,
                                                       self.uso_medicamentos,
                                                       self.id_pct)


class prontuario(models.Model):
    id_psi = models.AutoField(primary_key=True)
    motivo_consulta = models.TextField(blank=True, null=True)
    historico_tratamentos = models.TextField(blank=True, null=True)
    principais_sintomas = models.TextField(blank=True, null=True)
    observacoes_clinicas = models.TextField(blank=True, null=True)
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.id_psi,
                                               self.motivo_consulta,
                                               self.historico_tratamentos,
                                               self.principais_sintomas,
                                               self.observacoes_clinicas,
                                               self.id_pct)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.id_psi,
                                               self.motivo_consulta,
                                               self.historico_tratamentos,
                                               self.principais_sintomas,
                                               self.observacoes_clinicas,
                                               self.id_pct)


class Consultas(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    hora = models.TimeField()
    data = models.DateField()
    forma_pagamento = models.CharField(max_length=20, blank=True, null=True)
    responsavel_financeiro = models.CharField(max_length=100, blank=True, null=True)
    observacoes_gerais = models.TextField(blank=True, null=True)
    faltas = models.CharField(max_length=3, null=False)
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.id_consulta,
                                                   self.hora,
                                                   self.data,
                                                   self.forma_pagamento,
                                                   self.responsavel_financeiro,
                                                   self.observacoes_gerais,
                                                   self.faltas,
                                                   self.id_pct)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.id_consulta,
                                                   self.hora,
                                                   self.data,
                                                   self.forma_pagamento,
                                                   self.responsavel_financeiro,
                                                   self.observacoes_gerais,
                                                   self.faltas,
                                                   self.id_pct)


class uploadFile(models.Model):
    id_upfile = models.AutoField(primary_key=True)
    arquivo = models.FileField(upload_to='uploads/')
    nome_do_arquivo = models.CharField(max_length=255)
    data_upload = models.DateTimeField(auto_now_add=True)
    tamanho_do_arquivo = models.IntegerField()
    id_pct = models.ForeignKey("Clientes", on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.id_upfile,
                                               self.arquivo,
                                               self.nome_do_arquivo,
                                               self.data_upload,
                                               self.tamanho_do_arquivo,
                                               self.id_pct)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.id_upfile,
                                               self.arquivo,
                                               self.nome_do_arquivo,
                                               self.data_upload,
                                               self.tamanho_do_arquivo,
                                               self.id_pct)
