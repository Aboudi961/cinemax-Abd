
from models.films import Film
from models.vertoningen import Vertoning
from models.bestellingen import Bestellingen
from db.database import dbconn

class Datamanager:
    def alle_films(self):
        with dbconn() as cur:
            sql = "SELECT * FROM films"
            cur.execute(sql)
            rijen = cur.fetchall()
            films = [Film.from_dict(rij) for rij in rijen]
            return films

    def film_by_id(self, id):
        with dbconn() as cur:
            sql = "SELECT * FROM films WHERE id = ?"
            cur.execute(sql, [id])
            rij = cur.fetchone()

            if rij:
                film = Film.from_dict(rij)
                return film
            else:
                return None

    def film_by_IMDB_id(self, IMDB_id):
        with dbconn() as cur:
            sql = "SELECT * FROM films WHERE IMDB_id = ?"
            cur.execute(sql, [IMDB_id])
            rij = cur.fetchone()

            if rij:
                film = Film.from_dict(rij)
                return film
            else:
                return None

    def film_by_titel(self, zoekterm):
        with dbconn() as cur:
            sql = "SELECT * FROM films WHERE titel LIKE ?"
            cur.execute(sql, [zoekterm])
            rij = cur.fetchall()

            if rij:
                film = Film.from_dict(rij)
                return film
            else:
                return None

    def film_toevoegen(self, film):
        with dbconn() as cur:
            sql = "INSERT INTO films (titel, duur, IMDB_id) VALUES (?, ?, ?)"
            cur.execute(sql, [film.titel, film.duur, film.IMDB_id])

    def film_verwijderen(self, id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM films WHERE id = ?"
                cur.execute(sql, [id])
            else:
                raise ValueError

    def film_verwijderen(self, IMDB_id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM films WHERE id = ?"
                cur.execute(sql, [IMDB_id])
            else:
                raise ValueError


    def zoek_film_op_titel(self, zoekterm):
        with dbconn() as cur:
            film_titel = f"%{zoekterm}%"
            sql = "SELECT * FROM films WHERE titel LIKE ?"
            cur.execute(sql, [film_titel])
            rijen = cur.fetchall()

            films = [Film.from_dict(rij) for rij in rijen]
            return films


#datamanager voor vertoningen

    def alle_vertoningen(self):
        with dbconn() as cur:
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.film_id = films.id"
            cur.execute(sql)
            rijen = cur.fetchall()

            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def vertoningen_toevoegen(self, vertoningen):
        with dbconn() as cur:
            sql = "INSERT INTO vertoningen (tijdstip, zaalnummer, drie_D, film_id) VALUES (?, ?, ?, ?)"
            cur.execute(sql, [vertoningen.tijdstip, vertoningen.zaalnummer, vertoningen.drie_D, vertoningen.film_id ])


    def vertoningen_verwijderen(self, id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM vertoningen WHERE id = ?"
                cur.execute(sql, [id])
            else:
                raise ValueError



#datamanager voor bestellingen

    def alle_bestellingen(self):
        with dbconn() as cur:
            sql = "SELECT bestellingen.*,vertoningen*, films.* FROM bestellingen INNER JOIN vertoningen, films ON bestellingen.film_id = films.id AND vertoningen.film_id = film_id"
            cur.execute(sql)
            rijen = cur.fetchall()

            bestellingen = [Bestellingen.from_dict(rij) for rij in rijen]
            return bestellingen


    def bestellingen_toevoegen(self, bestellingen):
        with dbconn() as cur:
            sql = "INSERT INTO bestellingen ( aantal_kind, aantal_volwassen, totaalprijs, vertoning_id) VALUES (?, ?, ?, ?)"
            cur.execute(sql, [bestellingen.aantal_kind, bestellingen.aantal_volwassen, bestellingen.totaalprijs, bestellingen.vertoning_id ])


    def bestellingen_verwijderen(self, id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM bestellingen WHERE id = ?"
                cur.execute(sql, [id])
            else:
                raise ValueError