from models.vertoningen import Vertoning

class Bestellingen:
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
        return self.aantal_kind * 10 + self.aantal_volwassen * 15

    
        

    
    @classmethod
    def from_dict (cls, dict):
        aantal_kinderen = dict["aantal_kinderen"]
        aantal_volwassen = dict["aantal_volwassen"]
        totaalprijs = dict["totaalprijs"]
        vertoning_id = dict["vertoning_id"]

        return cls(aantal_kinderen, aantal_volwassen, totaalprijs, vertoning_id)
        