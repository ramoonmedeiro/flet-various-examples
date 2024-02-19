import flet as ft


def main(page: ft.Page):
    img = ft.Image(
        src="images/python-logo2.png",

        # mexer com os parâmetros de borda (caso houver)
        border_radius=ft.border_radius.only(
            top_left=10,
            top_right=20,
            bottom_left=10,
            bottom_right=20
        ),

        # altura
        height=100,

        # largura
        width=400,

        # nome da imagem pra quem for olhar 
        tooltip="Logo do Python"
    )

    page.add(img)

ft.app(target=main, assets_dir="assets")
