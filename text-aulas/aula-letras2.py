import flet as ft


def main(page: ft.Page):

    page.fonts = {
        "barret": "fonts/Barett Street.ttf"
    }

    t1 = ft.Text(

        # valor da str
        value="Olá mundo, seja bem vindo",
        # Tamanho da string
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        # cor do fundo onde a letra está
        bgcolor=ft.colors.BLACK,
        # cor da letra
        color=ft.colors.AMBER_300,

        # define o estilo da fonte
        # font_family="barret",

        # Mantém em itálico
        italic=True,

        # O número de linhas que é permitido
        # max_lines=2,

        # Indica que tem mais coisas após o max_lines ser atingido
        # overflow=ft.TextOverflow.ELLIPSIS

        # Não deixa o texto se adaptar ao layout
        no_wrap=True,

        # deixa selecionar o texto com o ctrl C
        selectable=True,

        # Define o tamanho da letra
        size=30,

        # Alinhar o texto
        text_align=ft.TextAlign.JUSTIFY,

        # Espessura da fonte
        weight=ft.FontWeight.BOLD
    )

    link_style = ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)
    link_style2 = ft.TextStyle(
        bgcolor=ft.colors.AMBER,
        color=ft.colors.RED,
        decoration=ft.TextDecoration.OVERLINE,
        decoration_color=ft.colors.RED,
        decoration_thickness=10,
        decoration_style=ft.TextDecorationStyle.WAVY,
        italic=True,
        size=40,
        weight=ft.FontWeight.BOLD
    )


    t2 = ft.Text(
        spans=[
            ft.TextSpan(text="Texto com link... ", style=link_style, url="https://google.com"),
            ft.TextSpan(text="continuação do texto "),
            ft.TextSpan(text="Final do texto!", style=link_style2)
        ],
        size=20,
        selectable=True
    )

    page.add(t1, t2)


ft.app(target=main, assets_dir="../assets")
