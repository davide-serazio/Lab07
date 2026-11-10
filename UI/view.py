import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

import flet as ft
from UI.alert import AlertManager


class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.alert = AlertManager(page)
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        # Sezione 1: intestazione
        self.txt_titolo = ft.Text(
            value="Biblioteche di Torino",
            size=38,
            weight=ft.FontWeight.BOLD
        )

        # Sezione 2: filtri
        self.dd_biblioteca = ft.Dropdown(
            label="Biblioteca",
            width=500,
            on_select=self.controller.seleziona_biblioteca # Quando l’utente seleziona una voce, Flet deve chiamare questo metodo del controller
        )

        self.dd_genere = ft.Dropdown(
            label="Genere",
            width=280,
            on_select=self.controller.seleziona_genere
        )

        # Sezione 3: libri
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",
            on_click=self.controller.mostra_libri
        )

        self.lista_libri = ft.ListView(
            height=350,
            spacing=10
        )

        # Cambio tema
        self.toggle_cambia_tema = ft.Switch(
            label="Tema scuro",
            value=True,
            on_change=self.cambia_tema
        )

        # Inserimento delle opzioni nei menu
        self.controller.popola_dropdown()

        # Layout della pagina
        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            ft.Divider(),
            ft.Row(
                controls=[self.dd_biblioteca, self.dd_genere],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),
            self.btn_mostra_libri,
            self.lista_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.toggle_cambia_tema.value
            else ft.ThemeMode.LIGHT
        )

        self.toggle_cambia_tema.label = (
            "Tema scuro"
            if self.toggle_cambia_tema.value
            else "Tema chiaro"
        )

        self.page.update()