import flet as ft
import datetime
import calendar
from db import buscar_por_mes_ano
from relatorio_utils import gerar_relatorio_excel


meses_pt = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}


def relatorio_view(page: ft.Page):

    mes_dd = ft.Dropdown(
        label="Selecione o mês",
        options=[ft.dropdown.Option(str(i), text=meses_pt[i]) for i in range(1, 13)],
        width=200
    )

    ano_dd = ft.Dropdown(
        label="Selecione o ano",
        options=[ft.dropdown.Option(str(y)) for y in range(2023, 2031)],
        width=200
    )

    psicologo_field = ft.TextField(label="Nome do Psicólogo", width=300)

    status_text = ft.Text("")

    def gerar_relatorio(e):
        if not mes_dd.value or not ano_dd.value or not psicologo_field.value:
            status_text.value = "⚠️ Preencha todos os campos antes de gerar o relatório!"
            page.update()
            return

        try:
            mes = int(mes_dd.value)
            ano = int(ano_dd.value)
            psicologo = psicologo_field.value.strip().replace(" ", "_")

            dados = buscar_por_mes_ano(mes, ano)

            if not dados:
                page.dialog = ft.AlertDialog(title=ft.Text("📭 Nenhum dado encontrado para esse mês e ano."))
                page.dialog.open = True
                status_text.value = "📭 Nenhum dado encontrado para esse mês e ano."
            else:
                path = gerar_relatorio_excel(dados, psicologo, mes, ano)
                if path:
                    page.dialog = ft.AlertDialog(title=ft.Text("✅ Arquivo salvo com sucesso!"))
                    page.dialog.open = True
                    status_text.value = f"✅ Relatório gerado com sucesso: {path}"
                else:
                    page.dialog = ft.AlertDialog(title=ft.Text("❌ Falha ao gerar o arquivo."))
                    page.dialog.open = True
                    status_text.value = "❌ Ocorreu um erro ao gerar o relatório."
        except Exception as err:
            page.dialog = ft.AlertDialog(title=ft.Text("❌ Erro ao gerar o relatório."))
            page.dialog.open = True
            status_text.value = f"❌ Erro: {err}"

        page.update()

    return ft.View(
        "/relatorio",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Gerar Relatório de Sessões", size=20),
                        psicologo_field,
                        ft.Row([mes_dd, ano_dd]),
                        ft.ElevatedButton("Gerar Relatório", icon="description", on_click=gerar_relatorio),
                        status_text,
                        ft.OutlinedButton("Voltar", icon="arrow_back", on_click=lambda e: page.go("/"))
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                width=500,
                padding=20,
                alignment=ft.alignment.center
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )