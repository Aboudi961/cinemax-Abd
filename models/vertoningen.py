
from models.films import Film

class Vertoning:
    def __init__(self,tijdstip, zaalnummer, drie_D, film_id ):
        self.tijdstip =tijdstip
        self.zaalnummer = zaalnummer
        self.drie_D = drie_D
        self.film_id = film_id

    @property
    def tijdstip(self):
        return self.tijdstip

    @property
    def zaalnummer(self):
        return self.zaalnummer

    @property
    def tijdstijp(self):
        return self.tijdstijp

    @property
    def drie_D(self):
        return self.drie_D

    @drie_D.setter
    def drie_D(self, drie_D):
        try:
            if drie_D:
                self.drie_D
        except ValueError:
            raise

    @property
    def film_id(self):
        return self.film_id

    @film_id.setter
    def film_id(self, film):
        try:
            if isinstance(film, Film):
                self.film_id
        except ValueError:
            raise


    @classmethod
    def from_dict(cls, dict):
        tijdstip = dict["tijdstip"]
        zaalnummer = dict["zaalnummer"]
        drie_D = dict["drie"]
        films = Film(dict["id"], dict["titel"], dict["duur"], dict["IMDB_id"])
        film_id = dict["film_id"]

        return cls(tijdstip, zaalnummer, drie_D, films, film_id )
        