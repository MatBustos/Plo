import flet as ft
from database.connection import get_connection

class ExercisesScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, muscle_group FROM exercises ORDER BY muscle_group, name")
        exercises = cursor.fetchall()
        conn.close()

        return ft.ListView(
            expand=True,
            spacing=10,
            controls=[
                ft.Text("Ejercicios", size=28, weight=ft.FontWeight.BOLD),
                ft.Text(f"{len(exercises)} ejercicios disponibles", size=14, color=ft.Colors.GREY_400),
                ft.Divider(),
            ] + [
                ft.ListTile(
                    title=ft.Text(name),
                    subtitle=ft.Text(muscle_group, size=12, color=ft.Colors.GREY_400),
                    leading=ft.Icon(ft.Icons.FITNESS_CENTER)
                ) for name, muscle_group in exercises
            ]
        )
