import flet as ft


def home_view(page: ft.Page):
    return ft.View(
        "/",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("PsyTrack", size=30, font_family="arial", italic=True),
                        ft.ElevatedButton(
                            "Cadastrar Nova Sessão",
                            on_click=lambda e: page.go("/cadastrar"),
                            icon="add",
                            scale=1.0
                        ),
                        ft.ElevatedButton(
                            "Emitir Relatório",
                            on_click=lambda e: page.go("/relatorio"),
                            icon="article"
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=400,
                padding=20,
                alignment=ft.alignment.center
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )