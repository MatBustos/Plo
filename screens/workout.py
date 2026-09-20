import flet as ft

class WorkoutScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Workout", size=28, weight=ft.FontWeight.BOLD),
                ft.Text("No hay workout activo", size=16, color=ft.Colors.GREY_400),
            ]
        )        
