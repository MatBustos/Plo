import flet as ft

class HistoryScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Historial", size=28, weight=ft.FontWeight.BOLD),
                ft.Text("Sin entrenamientos registrados", size=16, color=ft.Colors.GREY_400),
            ]
        )
