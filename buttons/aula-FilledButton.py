import flet as ft


def main(page: ft.Page):
    btn = ft.FilledButton(text="Aperte aqui")
    btn2 = ft.FilledButton(text="Aperte aqui", icon=ft.icons.STAR)
    btn3 = ft.FilledButton(text="Aperte aquui", icon=ft.icons.STAR, icon_color=ft.colors.AMBER)

    style = ft.ButtonStyle(
        padding=50,
        animation_duration=500,
        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(width=5, color=ft.colors.RED),
            ft.MaterialState.HOVERED: ft.BorderSide(width=10, color=ft.colors.GREEN)
        },
        # shape=ft.RoundedRectangleBorder(radius=0)
        shape={
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=0),
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30)
        },
    )


    btn4 = ft.FilledButton(
        text="Aperto aqui",
        style=style,
        url="https://google.com",
        tooltip="Aperte para mudar de site"
    )


    page.add(btn, btn2, btn3, btn4)

ft.app(target=main, assets_dir="../assets")
