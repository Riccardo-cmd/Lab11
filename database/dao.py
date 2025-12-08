from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def getAllRifugi():
        conn = DBConnect.get_connection()
        result = []
        query = """
                SELECT *
                FROM rifugio
                """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(Rifugio(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(year):
        """
        Recupera tutti i sentieri validi fino all'anno selezionato.
        """
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """
                    SELECT * FROM connessione 
                    WHERE anno <= %s
                    """

        cursor.execute(query, (year,))
        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result