import flet as ft
import random

def main(page: ft.Page):
    
    # appconfig
    page.title = "My First App"  # タイトル

    page.window_width = 500  # 幅
    page.window_height = 500  # 高さ
    page.window_minimizable = False  # 最小化ボタン
    page.window_maximizable = False  # 最大化ボタン
    page.window_resizable = False  # ウィンドウサイズ変更可否

    page.bgcolor = ft.colors.BLACK12  # ウィンドウ背景色

    page.update()  # プロパティ変更した場合は update()
    # appconfig

    li = ['PNG\slot01.png', 'PNG\slot02.png', 'PNG\slot03.png',
          'PNG\slot04.png', 'PNG\slot05.png', 'PNG\slot06.png',
          'PNG\slot07.png']

    def btn_clicked_1(e):
        img_1.src= random.choice(li)
        img_2.src= random.choice(li)
        img_3.src= random.choice(li)
        page.update()

    def btn_clicked_2(e):
        img_2.src= random.choice(li)
        page.update()

    def btn_clicked_3(e):
        img_3.src= random.choice(li)
        page.update()

    btn_1 = ft.IconButton(
        icon=ft.icons.REFRESH,
        icon_color='blue400',
        icon_size=50,
        tooltip='回す',
        on_click=btn_clicked_1
    )

    btn_2 = ft.IconButton(
        icon=ft.icons.SETTINGS_BACKUP_RESTORE,
        icon_color='blue400',
        icon_size=50,
        tooltip='回す',
        on_click=btn_clicked_2
    )

    btn_3 = ft.IconButton(
        icon=ft.icons.SETTINGS_BACKUP_RESTORE,
        icon_color='blue400',
        icon_size=50,
        tooltip='回す',
        on_click=btn_clicked_3
    )

    img_1 = ft.Image(
        src='PNG\slot01.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    img_2 = ft.Image(
        src='PNG\slot01.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    img_3 = ft.Image(
        src='PNG\slot01.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    txt = ft.Text() 

    page.add(
        ft.Row(
            [
                img_1,
                img_2,
                img_3
            ]
            , alignment=ft.MainAxisAlignment.CENTER
            ),
        ft.Row(
            [
                btn_1,
                # btn_2,
                # btn_3
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)