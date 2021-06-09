class Film:



    def __init__(self,id, titel, duur, IMDB_id ):
        self.id = id
        self.titel = titel
        self._duur = duur
        self._IMDB_id = IMDB_id



    @property
    def duur(self):
        return self._duur

    @duur.setter
    def duur(self, waarde):
        try:
            self._duur = int(waarde)
        except ValueError:
            raise

    @property
    def IMDB_id(self):
        return self.IMDB_id

    @IMDB_id.setter
    def IMDB_id(self, code):
        try:
            if code[0:2] == "tt":
                self._IMDB_id 

        except ValueError:
            raise

    @classmethod
    def from_dict(cls, dict):
        id = dict["id"]
        titel = dict["titel"]
        duur = dict["duur"]
        IMDB_id = dict["IMDB_id"]

        return cls(id, titel, duur, IMDB_id)
        
    
    