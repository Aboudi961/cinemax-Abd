
from models.films import Film

class Vertoning:
    def __init__(self, id, tijdstip, zaalnummer, drie_D, film_id ):
        self._id = id
        self._tijdstip = tijdstip
        self._zaalnummer = zaalnummer
        self._drie_D = drie_D
        self._film_id = film_id

    @property
    def id(self):
        return self._id

    # @property
    # def tijdstip(self):
    #     return self._tijdstip

    @property
    def zaalnummer(self):
        return self._zaalnummer

    
    @property
    def drie_D(self):
        if self.drie_D == "ja":
            return ("De film in 3D vertoont")
        else:
            return ("De film wordt niet in 3D vertoont ")

    

    @property
    def film_id(self):
        return self._film_id


    @classmethod
    def from_dict(cls, dict):
        id = dict["id"]
        tijdstip = dict["tijdstip"]
        zaalnummer = dict["zaalnummer"]
        drie_D = dict["drie_D"]
        film_id = Film(dict["titel"], dict["film_id"])

        return cls(id, tijdstip, zaalnummer, drie_D, film_id )
        