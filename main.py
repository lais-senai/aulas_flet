import flet as ft
# IMPORTA BIBLIOTECA FLET E CRIA UM APELIDO(ALIAS)

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet" #DEFINE O TÍTULO DA JANELA
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text("Bem-Vindo ao meu app!!!"),
        ft.Text("Aqui você pode criar o que quiser!!")
    )

ft.run(main)