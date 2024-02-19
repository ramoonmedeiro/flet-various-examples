import flet as ft


def main(page: ft.Page):

    page.spacing = 50

    btn1 = ft.ElevatedButton(text="Clique aqui")
    btn2 = ft.ElevatedButton(text="Botão inativo", disabled=True)
    btn3 = ft.ElevatedButton(text="Botão com ícone", icon=ft.icons.FAVORITE)
    btn4 = ft.ElevatedButton(
        # texto do botão
        text="Demais propriedades",
        # Cor de fundo do botão
        bgcolor=ft.colors.BLACK,
        # Cor das letras do botão
        color=ft.colors.WHITE,
        # Inserindo ícone
        icon=ft.icons.FAVORITE_BORDER,
        # Mudando a cor apenas do icon
        icon_color=ft.colors.AMBER,
        # inserir elemento de texto que ajude o user saber o que o botão faz
        tooltip="Olá, eu sou o botão",
        # ao ser acionado, o botão direciona para alguma url
        url="https://google.com"
        )

    style = ft.ButtonStyle(
        # Cor do texto do botão dada uma ação do mouse
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.GREEN

        },
        # Cor do fundo do botão dada um ação do mouse
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.PINK,
            ft.MaterialState.DEFAULT: ft.colors.AMBER
        },
        # Mudando tamanho do botão dada uma ação do mouse
        padding={
            ft.MaterialState.HOVERED: 20,
            ft.MaterialState.DEFAULT: 10
        },
        # Tempo em MS para uma animação para a mudança de cor do botão dada uma ação
        animation_duration=1000,
        # Mudando borda do botão
        side={
            ft.MaterialState.HOVERED: ft.BorderSide(
                width=1,
                color=ft.colors.BLUE
            ),
            ft.MaterialState.DEFAULT: ft.BorderSide(
                width=4,
                color=ft.colors.ORANGE
            ),
        },
        # Forma do botão
        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
            ft.MaterialState.DEFAULT: ft.ContinuousRectangleBorder(radius=20)
        }


    )

    btn5 = ft.ElevatedButton(
        text="Botão com estilo personalizado",
        style=style
    )

    page.add(btn1, btn2, btn3, btn4, btn5)

    def button_clicked(e):
        # e.control é a mesma coisa que o clique do usuário no botão para este caso
        e.control.data += 1
        text.value = f"Botão acionado {e.control.data} vezes"
        text.update()
        btn.update()

    # Botão com trigger
    btn = ft.ElevatedButton(
        text="Botão com contagem de cliques",
        on_click=button_clicked,
        data=0
    )

    text = ft.Text()

    page.add(btn, text)



ft.app(target=main, assets_dir="assets")
