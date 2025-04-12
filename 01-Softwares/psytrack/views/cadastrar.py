import flet as ft
import datetime
from db import inserir_sessao


def cadastrar_view(page: ft.Page):

    # == Campos do formulário ==
    nome_field = ft.TextField(label="Nome do Paciente", width=400)
    data_field = ft.TextField(label="Data de atendimento", width=400, hint_text="DD/MM/AAAA")

    realizada_dd = ft.Dropdown(
        label="Sessão Realizada",
        options=[ft.dropdown.Option(text=v) for v in ["Sim", "Não", "Remarcado"]],
        width=400
    )

    justificativas = [
        "Realizado | Cobrar Normalmente",
        "Falta Sem Aviso Prévio de 24h | Cobrar Normalmente",
        "Falta Sem Aviso Prévio Com Justificativa | Não Cobrar",
        "Falta Com Aviso Prévio de 24h | Não Cobrar, Remarcar.",
        "Desmarque do Profissional (informar motivo) | Não Cobrar",
    ]
    justificativas_dd = ft.Dropdown(
        label="Justificativas",
        options=[ft.dropdown.Option(text=j) for j in justificativas],
        width=400
    )

    comentarios_field = ft.TextField(label="Comentários", multiline=True, width=400, max_lines=3)

    # == Função salvar ==
    def salvar_sessao(e):
        if not nome_field.value or not data_field.value or not realizada_dd.value or not justificativas_dd.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos obrigatórios!"))
            page.snack_bar.open = True
            page.update()
            return

        inserir_sessao(
            paciente=nome_field.value,
            data=data_field.value,
            realizada=realizada_dd.value,
            justificativa=justificativas_dd.value,
            comentarios=comentarios_field.value or ""
        )

        page.snack_bar = ft.SnackBar(ft.Text("Sessão Salva com Sucesso!"))
        page.snack_bar.open = True
        page.update()

        # Limpa os campos
        nome_field.value = ""
        data_field.value = ""
        realizada_dd.value = ""
        justificativas_dd.value = ""
        comentarios_field.value = ""
        page.update()

    # == Retorno da View com Container ==
    return ft.View(
        "/cadastrar",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Cadastro de Sessão Clínica", size=20),
                        nome_field,
                        data_field,
                        realizada_dd,
                        justificativas_dd,
                        comentarios_field,
                        ft.Row([
                            ft.FilledButton("Salvar Sessão", icon="save", on_click=salvar_sessao),
                            ft.OutlinedButton("Voltar", icon="arrow_back", on_click=lambda e: page.go("/"))
                        ])
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=300,
                padding=20,
                alignment=ft.alignment.center
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )