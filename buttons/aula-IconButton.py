
import flet as ft


def main(page: ft.Page):
    btn = ft.IconButton(
        icon=ft.icons.DELETE_FOREVER,
        icon_color=ft.colors.PINK,
        icon_size=100,
        tooltip="Deletar uma ação"
    )

    def play_and_pause(e):
        e.control.selected = not e.control.selected
        e.control.update()

    btn2 = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE,
        selected_icon=ft.icons.PAUSE_CIRCLE,
        selected=False,
        icon_size=100,
        on_click=play_and_pause,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.SELECTED: ft.colors.RED,
                ft.MaterialState.DEFAULT: ft.colors.BLACK
        }
    ))

    page.add(btn, btn2)

ft.app(target=main, assets_dir="../")