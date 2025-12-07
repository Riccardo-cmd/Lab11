from database.DB_connect import DBConnect


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    def getAllRifugi(self, year):
        conn = DBConnect.get_connection()
        query = """
                SELECT DISTINCT r.*
                FROM rifugio r , connessione c
                WHERE (c.id_rifugio1=r.id  OR c.id_rifugio2=r.id)
                AND c.anno<=%s 
                """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (year,))

        result = []
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    def getAllConnessioni(self, year):
        conn = DBConnect.get_connection()
        query = """
                SELECT DISTINCT c.*
                FROM rifugio r , connessione c
                WHERE (c.id_rifugio1=r.id  OR c.id_rifugio2=r.id)
                AND c.anno<=%s 
                """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (year,))

        result = []
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
