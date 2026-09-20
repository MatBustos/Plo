import flet as ft 
from components.theme import apply_theme
from screens.home import HomeScreen
from components.bottom_nav import BottomNav

def main(page: ft.Page):
    apply_theme(page)
    page.title = "Plo"
    
    home = HomeScreen(page)
    nav = BottomNav(page)
    
    page.navigation_bar = nav.build()
    
    page.add(
        ft.SafeArea(
            content=home.build()
        )
    )

ft.run(main)


