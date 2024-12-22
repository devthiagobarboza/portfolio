import docx.opc.exceptions
import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, TextField, RadioGroup, Column, Dropdown, dropdown, Row, Banner, Icon, colors, icons, TextButton
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
from docxtpl import DocxTemplate
from pathlib import Path
import os


def main(page: Page) -> None:
    page.title = 'Gerador de Certificados | IBMR'
    page.window_width = 650
    page.window_height = 650

    informacoes_gerais = {
       'titulo_da_palestra': '',
       'data_da_realizacao': '',
       'carga_horaria': '',
       'unidade_curricular': '',
       'coordenador_de_grande_area': '',
       'coordenador_adjunto': '' ,
       'nome_do_aluno': '',
       'nome_do_palestrante': '',

    }

    #configuraçao dos modelos de certificados
    template_palestrante = DocxTemplate(os.path.join(os.getcwd(), "assets/modelo_certificado/palestrante/certificado_palestrante.docx"))
    output = '/certificados'
    cria_pasta_certificados = f"{output}/palestrante/{informacoes_gerais['titulo_da_palestra']}"
    pasta_palestrante = f"./{output}/palestrante/{informacoes_gerais['nome_do_palestrante']}"
    caminho_da_pasta_palestrante = Path(pasta_palestrante)



    #Entrada de dados
    titulo_da_palestra = TextField(label='Título da Palestra')
    data_da_realizacao = TextField(label='Data da realização')
    carga_horaria = TextField(label='Carga horária')
    unidade_curricular = TextField(label='Unidade Curricular')
    coordenador_de_grande_area = TextField(label='Coordenador(a) de Grande Área 1/IBMR')
    coordenador_adjunto = TextField(label='Coordenador Adjunto')
    nome_do_aluno = TextField(label='Nome do Aluno')
    nome_do_palestrante = TextField(label='Nome do Palestrante')




    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Gerar Certificado - Individual | Em Lote'), bgcolor='blue'),


                    ft.Row(

                        controls=[
                            ElevatedButton(
                                           text='Individual - Aluno',
                                           scale=1.2,
                                           on_click=lambda _: page.go('/gerar_certificado_individual_aluno'), icon="add_box_rounded", ),
                            ElevatedButton(text='Individual - Palestrante',
                                           scale=1.2,

                                           on_click=lambda _: page.go('/gerar_certificado_individual_palestrante'), icon="add_box_rounded"),

                        ], alignment=MainAxisAlignment.SPACE_AROUND,


                    ),
                    ft.Row(
                        controls=[
                            ElevatedButton(text='Em lote - Aluno',
                                           scale=1.2,
                                           on_click=lambda _: page.go('/gerar_certificado_em_lote_aluno'), icon="animation_rounded"),
                            ElevatedButton(text='Em lote - Palestrante',
                                           scale=1.2,
                                           on_click=lambda _: page.go('/gerar_certificado_em_lote_palestrante'), icon="animation_rounded"),

                        ], alignment=MainAxisAlignment.SPACE_AROUND,

                    )],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )


        # Tela Gerar Certificado individual aluno
        if page.route == '/gerar_certificado_individual_aluno':
            atualiza_form()
            page.views.append(
                View(
                    auto_scroll=False,
                    route='/gerar_certificado_individual_aluno',
                    controls=[
                        AppBar(title=Text('IBMR - Certificado Aluno'), bgcolor='purple'),
                        Text(value='Gerar Certificado Individual Aluno', size=30),
                        Row(
                            controls = [nome_do_aluno]),

                        Row(
                            controls=[
                            titulo_da_palestra

                        ]),
                        Row(
                            controls=[unidade_curricular]
                        ),
                        Row(
                            controls=[
                                data_da_realizacao,
                                carga_horaria,
                            ]),
                        Row(
                            controls=[
                                coordenador_de_grande_area,
                                coordenador_adjunto,
                            ]
                        ),

                        Row(
                            spacing=30,
                            controls=[
                                ElevatedButton(text='Voltar', on_click=lambda _: page.go('/')),
                                ElevatedButton(text='Gerar', on_click=lambda _: gera_certificado_aluno()),
                                ElevatedButton(text='Novo', on_click=lambda _: atualiza_form()),
                            ], alignment=MainAxisAlignment.CENTER
                        )],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26,
                    scroll=ft.ScrollMode.ALWAYS
                )

            )



        #Tela Gerar Certificado individual Palestrante
        if page.route == '/gerar_certificado_individual_palestrante':
            atualiza_form()
            page.views.append(
                View(
                    route='/gerar_certificado_individual_palestrante',
                    controls=[
                        AppBar(title=Text('Gerar certificado individual'), bgcolor='blue'),
                        Text(value='Gerar certificado individual', size=30),
                        Row(
                            controls=[nome_do_palestrante]
                        ),
                        Row(
                            controls=[titulo_da_palestra
                                      ]
                        ),
                        Row(
                            controls=[unidade_curricular]
                        ),
                        Row(
                            controls=[data_da_realizacao,
                                carga_horaria,
                            ]
                        ),
                        Row(
                            controls=[
                                coordenador_de_grande_area,
                                coordenador_adjunto
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(text='Voltar', on_click=lambda _: page.go('/')),
                                ElevatedButton(text='Gerar', on_click=lambda _: gera_certificado_palestrante()),
                                ElevatedButton(text='Novo', on_click=lambda _: atualiza_form()),
                            ],  alignment=CrossAxisAlignment.CENTER,
                                spacing=26,
                                scroll=ft.ScrollMode.ALWAYS

                        )
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26,
                    scroll=ft.ScrollMode.ALWAYS
                )
            )

        #Gerar certificado em lote
        if page.route == '/gerador_certificado_em_lote':
            page.views.append(
                View(
                    route='/gerador_certificado_em_lote',
                    controls=[
                        AppBar(title=Text('Gerar certificado em lote'), bgcolor='blue'),
                        Text(value='Gerar certificado em lote', size=30),
                        ElevatedButton(text='Voltar', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )

        page.update()



    def gera_certificado_aluno():
        informacoes_gerais['nome_do_aluno'] = titulo_da_palestra.value
        informacoes_gerais['unidade_curricular'] = unidade_curricular.value
        informacoes_gerais['titulo_da_palestra'] = titulo_da_palestra.value
        informacoes_gerais['data_da_realizacao'] = data_da_realizacao.value
        informacoes_gerais['coordenador_de_grande_area'] = coordenador_de_grande_area.value
        informacoes_gerais['coordenador_adjunto'] = coordenador_adjunto.value

        context = {
            'name': informacoes_gerais['nome_do_aluno'],
            'uc': informacoes_gerais['unidade_curricular'],
            'title': informacoes_gerais['titulo_da_palestra'],
            'date': informacoes_gerais['data_da_realizacao'],
            'head': informacoes_gerais['coordenador_de_grande_area'],
            'mentor': informacoes_gerais['coordenador_adjunto'],
        }

        for val in context.values():
            if not val:
                page.banner.open = True
                page.update()
                return
        try:

            template_palestrante.render(context)
            template_palestrante.save(f"..{output}/aluno/{informacoes_gerais['titulo_da_palestra'].capitalize()}/{informacoes_gerais['nome_do_aluno']}.docx")
            open_dlg()



        except docx.opc.exceptions.PackageNotFoundError as e:
            print(f"Error: {e}")


    def gera_certificado_palestrante():
        informacoes_gerais['titulo_da_palestra'] = titulo_da_palestra.value
        informacoes_gerais['unidade_curricular'] = unidade_curricular.value
        informacoes_gerais['titulo_da_palestra'] = titulo_da_palestra.value
        informacoes_gerais['data_da_realizacao'] = data_da_realizacao.value
        informacoes_gerais['coordenador_de_grande_area'] = coordenador_de_grande_area.value
        informacoes_gerais['coordenador_adjunto'] = coordenador_adjunto.value
        informacoes_gerais['nome_do_palestrante'] = nome_do_palestrante.value
        context = {
            'name': informacoes_gerais['nome_do_palestrante'],
            'uc': informacoes_gerais['unidade_curricular'],
            'title': informacoes_gerais['titulo_da_palestra'],
            'date': informacoes_gerais['data_da_realizacao'],
            'head': informacoes_gerais['coordenador_de_grande_area'],
            'mentor': informacoes_gerais['coordenador_adjunto'],
        }

        for val in context.values():
            if not val:
                page.banner.open = True
                page.update()
                return
        try:
            if not Path.exists(caminho_da_pasta_palestrante):
                caminho_da_pasta_palestrante.mkdir(parents=True)
            print(f"Pasta '{caminho_da_pasta_palestrante}' criada com sucesso")


            template_palestrante.render(context)
            #template_palestrante.save(f".{output}/palestrante/{informacoes_gerais['titulo_da_palestra']}/{informacoes_gerais['nome_do_palestrante']}.docx")

            #template_palestrante.save(f"../{output}/{informacoes_gerais['nome_do_palestrante']}.docx")
            template_palestrante.save(f"./{output}/palestrante/{informacoes_gerais['nome_do_palestrante']}.docx")
            open_dlg()


        except docx.opc.exceptions.PackageNotFoundError as e:
            print(f"Error: {e}")

        except OSError as fo:
            print("Falha na criaçao da pasta", fo)



    def close_dlg():
        dlg.open = False
        page.update()

    dlg = ft.AlertDialog(
        title=Text('Certificado Gerado com Sucesso!!'),
        actions=[TextButton('OK', on_click=lambda _: close_dlg())],
    )


    def open_dlg():
        page.dialog = dlg
        dlg.open = True
        page.clean()
        page.update()

    def atualiza_form():
        titulo_da_palestra.value = str('')
        nome_do_palestrante.value = str('')
        titulo_da_palestra.value = str('')
        carga_horaria.value = str('')
        data_da_realizacao.value = str('')
        unidade_curricular.value = str('')
        coordenador_de_grande_area.value = str('')
        coordenador_adjunto.value = str('')
        page.update()
        pass



    def fechar_banner():
        page.banner.open = False
        page.update()

    page.banner = Banner(
        bgcolor=ft.colors.RED_ACCENT_400,
        leading=ft.Icon(ft.icons.DANGEROUS_SHARP, color=colors.AMBER, size=40),
        content=Text('Todos os campos são de preenchimento obrigatório.', color='black'),
        actions=[
            TextButton("Ok", on_click=lambda _: fechar_banner())],

    )


    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()

ft.app(target=main)
