import flet as ft
from datetime import datetime

DAYS_ES = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

class HomeScreen:
    def __init__(self, page):
        self.page = page
    
    def build(self):
        today = datetime.now() 
        day_name = DAYS_ES[today.weekday()]
        
        return ft.Column(
            controls=[
                ft.Text(
                    day_name,
                    size=32,
                    weight=ft.FontWeight.BOLD),
                
                ft.Text(
                    "Sin plan hoy",
                    size=16,
                    color=ft.Colors.GREY_400),
                
                ft.Button(
                    content=ft.Text("Empezar entrenamiento"),
                    width=300,
                    height=50,
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE
                ),
                
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "ÚLTIMO ENTRENAMIENTO",
                                    size=12,
                                    color=ft.Colors.GREY_400
                                ),
                                ft.Text(
                                    "18/09 - Push Day",
                                    size=16
                                ),
                                ft.Text(
                                    "6 ejercicios, 24 series",
                                    size=14
                                )
                            ]
                        ),
                        padding=20,
                    )
                )
            ]
        )
        
