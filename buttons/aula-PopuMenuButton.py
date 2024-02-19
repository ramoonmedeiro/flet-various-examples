import flet as ft


def main(page: ft.Page):
    pb = ft.PopupMenuButton(
        icon=ft.icons.MENU,
        items=[
            ft.PopupMenuItem(text="item 1"),
            ft.PopupMenuItem(text="item 2"),
            ft.PopupMenuItem(text="item 3", icon=ft.icons.POWER),
        ]
    )

    page.add(pb)


ft.app(target=main)
