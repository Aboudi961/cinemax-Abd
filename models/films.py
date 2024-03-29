class Film:



    def __init__(self, titel, duur, IMDB_id ):
        
        self.titel = titel
        self._duur = duur
        self.IMDB_id = IMDB_id


    def __str__(self):
        return self.titel

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
        return self._IMDB_id 

    @IMDB_id.setter
    def IMDB_id(self, IMDB_id):
        try:
            if IMDB_id[0:2] == "tt":
                self._IMDB_id = IMDB_id

        except ValueError:
            raise

    @classmethod
    def from_dict(cls, dict):
       
        titel = dict["titel"]
        duur = dict["duur"]
        IMDB_id = dict["IMDB_id"]

        return cls(titel, duur, IMDB_id)
        
    
    