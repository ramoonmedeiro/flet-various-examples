import flet as ft


def main(page: ft.Page):
    # Mudando cor de backgorund
    page.bgcolor = ft.colors.AMBER
    # Mudando no eixo X
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    # Mudando no eixo Y
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Trabalhando com bordas
    # page.padding = ft.padding.symmetric(vertical=100, horizontal=10)
    page.padding = ft.padding.only(top=10, left=10, right=10, bottom=10)

    # Determina o numero de pixels que um elemento e outro terá como espaço
    page.spacing = 100

    # inserindo título na página
    page.title = "Flet APP"

    # Adicionando componentes
    page.add(
        # Adicionando mensagem em texto
        ft.Text(value="Olá Mundo!!"),
        # adicionando texto, mas com fundo local
        ft.Container(content=ft.Text("olá mundooooo!"), bgcolor=ft.colors.BLACK12)
    )

    # Atualizando a página
    page.update()

ft.app(target=main)
