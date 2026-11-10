from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""
# Un DAO, cioè Data Access Object, contiene le operazioni di accesso al database.

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection() # chiediamo una connessione e la conserviamo nella variabile cnx.
        cursor = cnx.cursor(dictionary=True) # Il cursore serve a eseguire la query e leggere le righe del risultato. Con dictionary=True, ogni riga viene restituita come dizionari

        query = """SELECT id, nome, indirizzo
                   FROM biblioteca"""
        cursor.execute(query) # invia la stringa al database.

        biblioteche = []

        for row in cursor: # Trasformiamo ogni riga in un oggetto Biblioteca
            biblioteca = Biblioteca(
                row["id"],
                row["nome"],
                row["indirizzo"]
            )
            biblioteche.append(biblioteca)

        cursor.close()
        cnx.close()

        return biblioteche
