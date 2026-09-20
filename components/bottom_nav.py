import flet as ft

class BottomNav:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.NavigationBar(
            selected_index=0,
            bgcolor=ft.Colors.SURFACE,
            indicator_color=ft.Colors.BLUE_700,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,      
                    selected_icon=ft.Icons.HOME,
                    label="Home"
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.LIST_OUTLINED,
                    selected_icon=ft.Icons.LIST,
                    label="Ejercicios",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FITNESS_CENTER_OUTLINED,
                    selected_icon=ft.Icons.FITNESS_CENTER,
                    label="Workouts",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.HISTORY_OUTLINED,
                    selected_icon=ft.Icons.HISTORY,
                    label="Historial",
                )
            ],
            on_change=self.on_nav_change
        )
        
    def on_nav_change(self, e):
        index = e.control.selected_index
        print(f"Selected index: {index}")
        
