import flet as ft


def main(page: ft.Page):
    btn1 = ft.TextButton(
        text="Editar",
        icon=ft.icons.EDIT,
        icon_color=ft.colors.BLACK,
        tooltip="Clique para editar"
    )

    page.add(btn1)


ft.app(target=main)