import flet as ft


def main(page: ft.Page):

    # definindo icon e propriedades
    icon1 = ft.Icon(
        name=ft.icons.FAVORITE,
        color=ft.colors.PINK,
        size=100,
        tooltip="Like"
        )

    icon2 = ft.Icon(
        name=ft.icons.AUDIOTRACK,
        color=ft.colors.GREEN_400,
        size=50,
        tooltip="Music"
    )

    icon3 = ft.Icon(
        name=ft.icons.BEACH_ACCESS,
        color=ft.colors.BLUE,
        size=80,
        tooltip="Praia"
    )

    page.add(icon1, icon2, icon3)


ft.app(target=main, assets_dir="assets")
