from django import forms
from . models import Clientes
ESTADO_CIVIL = (
    ('s', 'Solteiro'),
    ('c', 'Casado'),
    ('d', 'Divorciado'),
    ('v', 'Viúvo'),

)


class cadastra_clientes(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome', widget=forms.TextInput(attrs={'placeholder': 'Fritz'}))
    sobrenome = forms.CharField(max_length=100, label='Sobrenome', widget=forms.TextInput(attrs={'placeholder': 'Perls'}))
    nome_social = forms.CharField(max_length=100, label='Nome social', required=False)
    genero = forms.CharField(max_length=20, label='Gênero')
    data_nascimento = forms.DateField()
    cpf = forms.CharField(max_length=14, label='CPF')
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL, label='Estado civil')
    profissao = forms.CharField(max_length=20, required=False, label='Profissão')
    telefone_principal = forms.CharField(max_length=15, label='Telefone principal')
    telefone_emergencia = forms.CharField(max_length=15, required=False, label='Telefone de emergência')
    email = forms.EmailField(label='E-mail')
    observacoes = forms.CharField(widget=forms.TextInput(), label='Observações')

    class Meta:
        model = Clientes
        fields = '__all__'





