import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Cagar e acordar")
        )
    page.add(
        ft.Text("TararaTAMtararaTAM"),
        ft.Image(
            src="images/incrivelsus.png",
            height=200
        ),

        ft.Button(
            content="clique aqui",
            on_click=mostrar_mensagem
        )
        )
        
ft.run(main)