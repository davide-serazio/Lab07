import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    def popola_dropdown(self):
        self._view.dd_biblioteca.options.append(
            ft.dropdown.Option("Nessun filtro")
        )

        for biblioteca in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(
                    key=str(biblioteca.id),
                    text=biblioteca.nome
                )
            )

        self._view.dd_genere.options.append(
            ft.dropdown.Option("Nessun filtro")
        )

        for genere in self._model.get_generi():
            self._view.dd_genere.options.append(
                ft.dropdown.Option(genere)
            )

        self._view.dd_biblioteca.value = "Nessun filtro"
        self._view.dd_genere.value = "Nessun filtro"

    def seleziona_biblioteca(self, e):
        valore = self._view.dd_biblioteca.value

        if valore == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    def seleziona_genere(self, e):
        valore = self._view.dd_genere.value

        if valore == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        self._view.lista_libri.controls.clear()

        for libro in libri:
            self._view.lista_libri.controls.append(
                ft.Text(str(libro))
            )

        self._view.update()

        if len(libri) == 0:
            self._view.show_alert(
                "Nessun libro soddisfa i filtri selezionati."
            )