from models.vertoningen import Vertoning

class bestellingen:
    def __init__(self, aantal_kind, aantal_volwassen, totaalprijs, vertoning_id):
        self.aantal_kind = aantal_kind
        self.aantal_volwassen = aantal_volwassen
        self.totaalprijs = totaalprijs
        self.vertoning_id = vertoning_id

    @property
    def aantal_kinderen(self):
        return self.aantal_kinderen


    @property
    def aantal_volwassen(self):
        return self.aantal_volwassen

    @property
    def totaalprijs(self):
        return self.aantal_kind + self.aantal_volwassen

    @property
    def vertoning_id(self):
        return self.vertoning_id

    @vertoning_id.setter
    def vertoning_id(self, vertoning_id):
        try:
            if isinstance(vertoning_id, Vertoning):
                self.vertoning_id
        except ValueError:
            raise

    
    @classmethod
    def from_dict (cls, dict):
        aantal_kinderen = dict["aantal_kinderen"]
        aantal_volwassen = dict["aantal_volwassen"]
        totaalprijs = dict["totaalprijs"]
        vertoning_id = dict["vertoning_id"]

        return cls(aantal_kinderen, aantal_volwassen, totaalprijs, vertoning_id)
        