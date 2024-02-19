import flet as ft


def main(page: ft.Page):
    btn = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.GREEN,
        mini=False,
        shape=ft.CircleBorder(),
        tooltip="Cadastrar novo produto",
        on_click=lambda _: print("fui clicado")
    )

    page.add(btn)

ft.app(target=main, assets_dir="../")