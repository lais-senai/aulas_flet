import flet as ft


# HABILITAR O SCROLL DO MOUSE
# def main(page: ft.Page):
#     page.scroll = ft.ScrollMode.AUTO

#     for i in range(100):
#         page.add(ft.Text(f"Item {i}"))

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text(f"Item [i]") for i in range(100)
            ],
            height=300,
            scroll=ft.ScrollMode.ALWAYS
        )
    )


def main(page: ft.Page):
    page.add(
        ft.Column([
            ft.Text("Titulo do app", size=22, weight="bold"),
            ft.Row([
                ft.ElevatedButton("Botão 1"),
                ft.ElevatedButton("Botão 2"),
                ft.ElevatedButton("Botão 3"),
            ], spacing=10),
            ft.Text("Rodapé do app")
        ], spacing=20)
    )


ft.run(main)
