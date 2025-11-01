import flet as ft
from flet import Icons

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding=0

    def homepage():
        page.appbar = ft.AppBar(
            title=ft.Text("Score Sustentavel"),
            center_title=True,
            bgcolor=ft.Colors.INDIGO
        )

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(label='Questionario', icon=ft.Icons.BOOK),
                ft.NavigationBarDestination(label='Score', icon=ft.Icons.SCORE),
                ft.NavigationBarDestination(label='Perfil', icon=ft.Icons.PERSON),
            ]
        )

        page.add(
            ft.Text('Home Page')
        )

        page.update()


    def logincerto(e):
        if Usuario.value == "adm" and senha.value == "123":
            page.controls.clear()
            homepage()

            snackbar_sucess = ft.SnackBar(
                content=ft.Text("Login feito com sucesso"),
                bgcolor=ft.Colors.GREEN,
                show_close_icon=True,
            )
            page.overlay.append(snackbar_sucess)
            snackbar_sucess.open = True
            page.update()
        else:
            snackbar_error = ft.SnackBar(
                content=ft.Text("Credenciais invalidas", color=ft.Colors.WHITE, size=20),
                bgcolor=ft.Colors.RED,
                show_close_icon=True,
            )
            page.overlay.append(snackbar_error)
            snackbar_error.open = True
            page.update()

    Logintext = ft.Text(
        value="Login",
        size=30,
        width=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        italic=True ,
    )

    Usuario = ft.TextField(
        label="Usuario",
        prefix_icon=ft.Icons.PERSON,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.border_radius.all(10),
        border_color=ft.Colors.WHITE,
        border_width=2,
        width=300
    )

    senha = ft.TextField(
        label="Senha",
        prefix_icon=ft.Icons.PERSON,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.border_radius.all(10),
        border_color=ft.Colors.WHITE,
        border_width=2,
        password=True,
        can_reveal_password=True,
        width=300
    )

    Button_log = ft.ElevatedButton(
        text="Login",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        width=300,
        on_click=logincerto
    )

    page.add(
        ft.Container(
            #image_src='https://cdn.discordapp.com/attachments/1128864924282667010/1433934153426014238/uma-arvore-com-um-grande-tronco_691522-13547.webp?ex=69067ebf&is=69052d3f&hm=c403e5ad5c7d1fce384a983a90d14085703bbce7f474692c3ee36a15eb5e470e&',
            #opacity=0.8,
            #image_fit=ft.ImageFit.COVER,
            #expand=True,
            #alignment=ft.alignment.center,
            content=ft.Column(
                controls=[Logintext, Usuario, senha, Button_log,],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )
    page.update()

ft.app(main)