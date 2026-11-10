from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

from database.DB_connect import DBConnect
from model.libro_DTO import Libro


class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT id, titolo, autore, genere,
                          anno_pubblicazione, id_biblioteca
                   FROM libro"""
        cursor.execute(query)

        libri = []
        for row in cursor:
            libro = Libro(
                row["id"],
                row["titolo"],
                row["autore"],
                row["genere"],
                row["anno_pubblicazione"],
                row["id_biblioteca"]
            )
            libri.append(libro)

        cursor.close()
        cnx.close()
        return libri

    def get_generi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "SELECT DISTINCT genere FROM libro"
        cursor.execute(query)

        generi = []
        for row in cursor:
            generi.append(row["genere"])

        cursor.close()
        cnx.close()
        return generi