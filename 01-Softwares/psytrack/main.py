import flet as ft
from views.cadastrar import cadastrar_view
from views.relatorio import relatorio_view
from views.home import home_view
from db import criar_tabela


def main(page: ft.Page):
    page.window.height = 500
    page.window.width = 500
    page.padding = 25
    page.title = "Psytrack"
    page.scroll = ft.ScrollMode.AUTO
    page.window_resizable = False


    page.theme_mode = ft.ThemeMode.LIGHT

    criar_tabela()

    def route_change(e):
        page.views.clear()

        if page.route == '/':
            page.views.append(home_view(page))
        elif page.route == "/cadastrar":
            page.views.append(cadastrar_view(page))
        elif page.route == "/relatorio":
            page.views.append(relatorio_view(page))

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)

