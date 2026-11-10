from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO


class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    def get_libri_filtrati(self, biblioteca, genere):
        libri = self._libro_dao.get_libri()
        risultato = []

        for libro in libri:
            if (biblioteca is None or libro.id_biblioteca == biblioteca) and (
                genere is None or libro.genere == genere
            ):
                risultato.append(libro)

        return risultato

    def get_generi(self):
        return self._libro_dao.get_generi()

    def get_biblioteche(self):
        return self._biblioteca_dao.get_biblioteche() # diciamo: DAO, esegui il tuo metodo get_biblioteche()