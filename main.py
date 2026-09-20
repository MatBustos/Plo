import flet as ft 
from components.theme import apply_theme
from components.bottom_nav import BottomNav
from database.models import create_tables
from database.seed_data import seed_exercises

def main(page: ft.Page):
    apply_theme(page)
    page.title = "Plo"
    
    create_tables()
    seed_exercises()
    
    nav = BottomNav(page)
    page.navigation_bar = nav.build()
    
    page.add(
        ft.SafeArea(
            expand=True,
            content=nav.screens[0].build()
        )
    )

ft.run(main)


