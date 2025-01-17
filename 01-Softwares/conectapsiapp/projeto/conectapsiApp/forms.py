from django import forms
from .models import Clientes, Anamnese, Endereco, SessaoClinica
from django.forms import inlineformset_factory
from django_select2.forms import ModelSelect2Widget

ESTADO_CIVIL = (
    ('Solteiro', 'Solteiro'),
    ('Casado', 'Casado'),
    ('Separado', 'Separado'),
    ('Viuvo', 'Viúvo'),
)

GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('B', 'Bissexual'),
    ('T', 'Travesti'),
)

TIPO_ATENDIMENTO = (
    ('P', 'Particular'),
    ('Con', 'Convênio'),
    ('CR', 'Clinica React'),
    ('CN', 'Na Mesma Roda')
)

ALTA = (
    ('S', 'Sim'),
    ('N', 'Não')
)


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nome',
            'sobrenome',
            'nome_social',
            'genero',
            'data_nascimento',
            'cpf',
            'estado_civil',
            'conjuge_nome',
            'conjuge_idade',
            'conjuge_sexo',
            'filhos_nome',
            'filhos_idade',
            'filhos_sexo',
            'religiao',
            'escolaridade',
            'profissao',
            'telefone_principal',
            'telefone_emergencia',
            'email',
            'observacoes',
        ]
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'nome_social': 'Nome Social',
            'genero': 'Gênero',
            'data_nascimento': 'Data de Nascimento',
            'cpf': 'CPF',
            'estado_civil': 'Estado Civil',
            'conjuge_nome': 'Nome do Cônjuge',
            'conjuge_idade': 'Idade do Cônjuge',
            'conjuge_sexo': 'Sexo do Cônjuge',
            'filhos_nome': 'Nome do(s) Filho(s)',
            'filhos_idade': 'Idade do(s) Filho(s)',
            'filhos_sexo': 'Sexo do(s) Filho(s)',
            'religiao': 'Religião',
            'escolaridade': 'Escolaridade',
            'profissao': 'Profissão',
            'telefone_principal': 'Telefone Principal',
            'telefone_emergencia': 'Telefone de Emergência',
            'email': 'E-mail',
            'observacoes': 'Observações',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'nome_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Social'}),
            'genero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gênero'}, choices=GENEROS),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}, ),
            'estado_civil': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado civil'},
                                         choices=ESTADO_CIVIL),
            'conjuge_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do cônjuge'}),
            'conjuge_idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade do cônjuge'}),
            'conjuge_sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo do cônjuge'}),
            'filhos_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome dos filhos'}),
            'filhos_idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade dos filhos'}),
            'filhos_sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo dos filhos'}),
            'religiao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Religião'}),
            'escolaridade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escolaridade'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profissão'}),
            'telefone_principal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'telefone_emergencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@dominio.com'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações', 'rows': 4}),
        }


class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese
        fields = [
            'id_pct',
            'queixa_principal',
            'possibilidade_de_horarios',
            'fez_terapia_anterior',
            'quando_fez_terapia_anterior',
            'expectativa_e_objetivo_do_paciente',
            'sintomas_apresentados',
            'tipo_de_atendimento',
            'plano_de_saude',
            'numero_carteirinha',
            'historico_medico',
            'historico_familiar',
            'diagnosticos_preexistentes',
            'conceituacao_psicologica_do_caso',
            'transtornos_psiquiatricos_anteriores',
            'transtornos_psiquiatricos_familiares',
            'doenca_importante_que_teve',
            'uso_medicamentos',
            'uso_medicamentos_alternativos',
            'aplicacao_de_teste',
            'historico_da_queixa_quando_se_iniciou',
            'eventos_traumaticos_da_vida',
            'eventos_que_agravam_a_crise',
            'tentativa_de_suicidio',
            'uso_de_drogas',
            'relacionamentos_importantes_mae',
            'relacionamentos_importantes_pai',
            'relacionamentos_importantes_irmaos',
            'relacionamentos_importantes_filhos',
            'relacionamentos_importantes_outros',
            'observacao_sobre_dinamica_familiar_atual',
            'infancia_gravidez_planejada',
            'infancia_amamentacao',
            'infancia_estressores_crises',
            'infancia_transtornos_infantis',
            'infancia_comentarios',
            'adolescencia_experiencias_afetivas_marcantes',
            'adolescencia_experiencias_sexuais_marcantes',
            'adolescencia_independencia',
            'adolescencia_circulo_de_amizades',
            'vida_adulta_relacionamento_com_parceiro',
            'vida_adulta_vida_sexual_atual',
            'vida_adulta_situacao_financeira',
            'vida_adulta_abordo_espontaneo',
            'vida_adulta_apoio_social',
            'vida_adulta_outros_transtornos',
            'vida_adulta_principais_lazeres',
            'observacao_e_linguagem_nao_verbal',
            'atendimentos_prestados_profissional',
            'atendimentos_prestados_encaminhamentos',
            'atendimentos_prestados_terapeutica_utilizada',
            'atendimentos_prestados_destino_do_caso_alta',
            'atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao',
            'atendimentos_prestados_destino_do_caso_abandono',
            'atendimentos_prestados_destino_do_caso_outro_profissional',
            'atendimentos_prestados_destino_do_caso_interrompido',
            'atendimentos_prestados_destino_do_caso_melhoras_obtidas',
            'atendimentos_prestados_destino_do_caso_outras_obs',
        ]

        labels = {
            'id_pct': 'Selecione o paciente',
            'tipo_de_atendimento': 'Tipo de Atendimento',
            'plano_de_saude': 'Plano de Saúde',
            'numero_carteirinha': 'Número da Carteirinha',
            'historico_medico': 'Histórico Médico',
            'historico_familiar': 'Histórico Familiar',
            'diagnosticos_preexistentes': 'Diagnósticos Pré-existentes',
            'uso_medicamentos': 'Uso de Medicamentos',
            'uso_medicamentos_alternativos': 'Uso de Medicamentos Alternativos',
            'conceituacao_psicologica_do_caso': 'Conceituação Psicológica do Caso',
            'queixa_principal': 'Queixa Principal',
            'possibilidade_de_horarios': 'Possibilidade de Horários',
            'fez_terapia_anterior': 'Já fez terapia anteriormente?',
            'quando_fez_terapia_anterior': 'Quando fez terapia anteriormente?',
            'expectativa_e_objetivo_do_paciente': 'Expectativa e Objetivo do Paciente',
            'sintomas_apresentados': 'Sintomas Apresentados',
            'transtornos_psiquiatricos_anteriores': 'Transtornos Psiquiátricos Anteriores',
            'transtornos_psiquiatricos_familiares': 'Transtornos Psiquiátricos Familiares',
            'doenca_importante_que_teve': 'Doenças Importantes',
            'aplicacao_de_teste': 'Aplicação de Teste',
            'historico_da_queixa_quando_se_iniciou': 'Histórico da Queixa (Quando se Iniciou)',
            'eventos_traumaticos_da_vida': 'Eventos Traumáticos da Vida',
            'eventos_que_agravam_a_crise': 'Eventos que Agravam a Crise',
            'tentativa_de_suicidio': 'Tentativa de Suicídio',
            'uso_de_drogas': 'Uso de Drogas',
            'relacionamentos_importantes_mae': 'Mãe',
            'relacionamentos_importantes_pai': 'Pai',
            'relacionamentos_importantes_irmaos': 'Irmãos',
            'relacionamentos_importantes_filhos': 'Filhos',
            'relacionamentos_importantes_outros': 'Outros Importantes',
            'observacao_sobre_dinamica_familiar_atual': 'Observação Sobre Dinâmeica Familiar Atual',
            'infancia_gravidez_planejada': 'Gravidez(planejada ou não), Parto, Intercorrências Obstétricas',
            'infancia_amamentacao': 'Amamentação',
            'infancia_estressores_crises': 'Estressores na Infância, Crises',
            'infancia_transtornos_infantis': 'Outros Transtornos Infantis',
            'infancia_comentarios': 'Outros Comentários',
            'adolescencia_experiencias_afetivas_marcantes': 'Experiências Afetivas Marcantes',
            'adolescencia_experiencias_sexuais_marcantes': 'Experiências Sexuais Marcantes',
            'adolescencia_independencia': 'Indepêndencia/Primeiros empregos',
            'adolescencia_circulo_de_amizades': 'Círculo de amizades',
            'vida_adulta_relacionamento_com_parceiro': 'Relacionamento com Parceiros',
            'vida_adulta_vida_sexual_atual': 'Vida Sexual Atual',
            'vida_adulta_situacao_financeira': 'Situação Financeira',
            'vida_adulta_abordo_espontaneo': 'Abortos espontâneos/provocados',
            'vida_adulta_apoio_social': 'Apoio Social Disponível',
            'vida_adulta_outros_transtornos': 'Outros Transtornos Atuais',
            'vida_adulta_principais_lazeres': 'Principais Lazeres, Vida Social',
            'observacao_e_linguagem_nao_verbal': 'Observações',
            'atendimentos_prestados_profissional': 'Profissional',
            'atendimentos_prestados_encaminhamentos': 'Encaminhamentos Feitos',
            'atendimentos_prestados_terapeutica_utilizada': 'Terapêutica Utilizada',
            'atendimentos_prestados_destino_do_caso_alta': 'Alta',
            'atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao': 'Encaminhamento para outra '
                                                                                       'insituição (Qual?)',
            'atendimentos_prestados_destino_do_caso_abandono': 'Abandono (Motivo?)',
            'atendimentos_prestados_destino_do_caso_outro_profissional': ' Encaminhamento para outro profissional(Quem?)',
            'atendimentos_prestados_destino_do_caso_interrompido': 'Interrompido (Por que?)',
            'atendimentos_prestados_destino_do_caso_melhoras_obtidas': 'Melhoras Obtidas',
            'atendimentos_prestados_destino_do_caso_outras_obs': 'Outras Observações Importantes',
        }
        widgets = {
            'id_pct': ModelSelect2Widget(
                model=Clientes,
                search_fields=['nome__icontains', 'sobrenome__icontains'],
                attrs={'class': 'form-control',
                       'data-placeholder': 'Busque Por Nome, Sobrenome'}),
            'queixa_principal': forms.Textarea(attrs={'class': 'form-control',
                                                      'placeholder': 'Descreva a queixa principal',
                                                      'rows': 4}),
            'possibilidade_de_horarios': forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Possibilidade de Horários'}),
            'fez_terapia_anterior': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Fez Terapia Anteriormente?'}),
            'quando_fez_terapia_anterior': forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Quando Fez Terapia?'}),
            'expectativa_e_objetivo_do_paciente': forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Expectativa e Objetivo'}),
            'sintomas_apresentados': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Sintomas Apresentados'}),
            'tipo_de_atendimento': forms.Select(attrs={'class': 'form-control'}, choices=TIPO_ATENDIMENTO),
            'plano_de_saude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plano de Saúde'}),
            'numero_carteirinha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da Carteira'}),
            'historico_medico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Histórico Médico'}),
            'historico_familiar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Histórico Familiar'}),
            'diagnosticos_preexistentes': forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Diagnósticos Preexistentes'}),
            'conceituacao_psicologica_do_caso': forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Conceituação Psicológica do Caso'}),
            'transtornos_psiquiatricos_anteriores': forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Transtornos Psiquiátricos '
                                                                                          'Anteriores'}),
            'transtornos_psiquiatricos_familiares': forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Transtornos Psiquiátricos '
                                                                                          'Familiares'}),
            'doenca_importante_que_teve': forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Doença Importante Que Teve'}),
            'uso_medicamentos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Uso de Medicamentos'}),
            'uso_medicamentos_alternativos': forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Uso de Medicamentos Alternativos'}),
            'aplicacao_de_teste': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Aplicação de Teste? Qual Resultado?'}),
            'historico_da_queixa_quando_se_iniciou': forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Quando se iniciou?'}),
            'eventos_traumaticos_da_vida': forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Eventos Traumáticos de Vida'}),
            'eventos_que_agravam_a_crise': forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Eventos/fatores que precipitam/agravam crises'}),
            'tentativa_de_suicidio': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Tentativa de Suicídio?'}),
            'uso_de_drogas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Uso de Drogas'}),
            'relacionamentos_importantes_mae': forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Relacionamento com a Mãe'}),
            'relacionamentos_importantes_pai': forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Relacionamento com o Pai'}),
            'relacionamentos_importantes_irmaos': forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Relacionamento com Irmãos'}),
            'relacionamentos_importantes_filhos': forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Relacionamento com o Filhos'}),
            'relacionamentos_importantes_outros': forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Outros Relacionamentos '
                                                                                        'Importantes'}),
            'observacao_sobre_dinamica_familiar_atual': forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Observação dinâmica '
                                                                                              'familiar atual',
                                                                               'rows': 4}),
            'infancia_gravidez_planejada': forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Gravidez Planejada, parto, '
                                                                                 'intercorrências Obstétricas'}),
            'infancia_amamentacao': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Amamentação'}),
            'infancia_estressores_crises': forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Estressores na infância, crises'}),
            'infancia_transtornos_infantis': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'sono, psicomotor, gagueira, tique etc'}),
            'infancia_comentarios': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Comentários'}),
            'adolescencia_experiencias_afetivas_marcantes': forms.TextInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Experiências '
                                                                                                  'Afetivas '
                                                                                                  'Marcantes'}),
            'adolescencia_experiencias_sexuais_marcantes': forms.TextInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Experiências '
                                                                                                 'Sexuais Marcantes'}),
            'adolescencia_independencia': forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Independência/Primeiros Empregos'}),
            'adolescencia_circulo_de_amizades': forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Círculo de Amizades'}),
            'vida_adulta_relacionamento_com_parceiro': forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Relacionamento com '
                                                                                             'Parceiro'}),
            'vida_adulta_vida_sexual_atual': forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Vida Sexual Atual'}),
            'vida_adulta_situacao_financeira': forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Situação Financeira'}),
            'vida_adulta_abordo_espontaneo': forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Abortos Espontâneos/Provocados'}),
            'vida_adulta_apoio_social': forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Apoio Social Disponível'}),
            'vida_adulta_outros_transtornos': forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Outros transtornos: Sono, '
                                                                                    'Alimentação, tiques '
                                                                                    'etc'}),
            'vida_adulta_principais_lazeres': forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Principais Prazeres / '
                                                                                    'Vida Social'}),
            'observacao_e_linguagem_nao_verbal': forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Observações e '
                                                                                       'linguagem não verbal'}),
            'atendimentos_prestados_profissional': forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Atendimento '
                                                                                         'Prestado Profissional'}),
            'atendimentos_prestados_encaminhamentos': forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Encaminhamentos Feitos'}),
            'atendimentos_prestados_terapeutica_utilizada': forms.TextInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Terapêutica '
                                                                                                  'utilizada '
                                                                                                  '(exercícios, '
                                                                                                  'leituras, '
                                                                                                  'relaxamento etc'}),
            'atendimentos_prestados_destino_do_caso_alta': forms.Select(attrs={'class': 'form-control'}, choices=ALTA),
            'atendimentos_prestados_destino_do_caso_encaminhamento_outra_instituicao':
                forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Para Qual Outra Instituição Fora Encaminhado?'}),
            'atendimentos_prestados_destino_do_caso_abandono': forms.TextInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'Motivo do '
                                                                                                     'Abandono'}),
            'atendimentos_prestados_destino_do_caso_outro_profissional': forms.TextInput(attrs={'class': 'form-control',
                                                                                                'placeholder':
                                                                                                    'Encaminhado a '
                                                                                                    'Outro '
                                                                                                    'Profissional,'
                                                                                                    ' Quem?'}),
            'atendimentos_prestados_destino_do_caso_interrompido': forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Interrompido,'
                                                                                                         ' porquê?'}),
            'atendimentos_prestados_destino_do_caso_melhoras_obtidas': forms.TextInput(attrs={'class': 'form-control',
                                                                                              'placeholder':
                                                                                                  'Melhoras Obtidas'}),
            'atendimentos_prestados_destino_do_caso_outras_obs': forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Outras'
                                                                                                       'Observações '
                                                                                                       'Importantes'}),

        }


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'rua',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'cep',
        ]
        labels = {
            'rua': 'Rua',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': "Bairro",
            'cidade': "Cidade",
            'uf': 'UF',
            'cep': 'CEP',
        }
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complemento'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
        }


def get_endereco_formset(extra=1, can_delete=False):
    return inlineformset_factory(
        Clientes,
        Endereco,
        form=EnderecoForm,
        extra=extra,
        can_delete=can_delete)


EnderecoFormSet = inlineformset_factory(
    Clientes,
    Endereco,
    form=EnderecoForm,
    extra=1,
    can_delete=False)


class SessaoClinicaForm(forms.ModelForm):
    class Meta:
        model = SessaoClinica
        fields = [
            'id_pct',
            'objetivos',
            'data_atendimento',
            'numero_da_sessao',
            'pontos_importantes_da_sessao',
            'principais_sintomas',
            'observacoes_clinicas',
            'evolucao',
        ]
        labels = {
            'id_pct': 'Selecione o paciente',
            'objetivos': 'Objetivos',
            'data_atendimento': 'Data do Atendimento',
            'numero_da_sessao': 'Número da Sessão',
            'pontos_importantes_da_sessao': 'Pontos Importantes da Sessão',
            'principais_sintomas': 'Principais Sintomas',
            'observacoes_clinicas': 'Observações Clínicas',
            'evolucao': 'Evolução',
        }

        widget = {
            'id_pct': ModelSelect2Widget(
                model=Clientes,
                search_fields=['nome__icontains', 'sobrenome__icontains'],
                attrs={'class': 'form-control',
                       'data-placeholder': 'Busque Por Nome, Sobrenome'}),
            'objetivos': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Qual o ojetivo desse paciente?'}),
            'data_atendimento': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'O atendimento foi no dia?'}),
            'numero_da_sessao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estamos na sessão?'}),
            'pontos_importantes_da_sessao': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Isso é importante...'}),
            'principais_sintomas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O que sinto é ...'}),
            'observacoes_clinicas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observei que ...'}),
            'evolucao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Na sessão de hoje ... '}),

        }
