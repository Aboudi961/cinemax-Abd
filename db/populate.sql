INSERT INTO films(titel, duur, IMDB_id)
VALUES ("Inception", "148", "tt1375666"),
       ("myrobot", "49", "tt4568726"),
       ("1917", "119", "tt8579674")
;

INSERT INTO vertoningen (tijdstip, zaalnummer, drie_D, film_id)
VALUES ("2021-06-30", "7", "ja", 1),
       ("2021-07-15", "2", "nee", 2),
       ("2021-07-28", "5", "nee", 1)
;

INSERT INTO bestellingen (aantal_kind, aantal_volwassen, totaalprijs, vertoning_id)
VALUES ("1", "2", "50", 1 ),
       ("2", "1", "40", 2 ),
       ("3", "2", "45", 3 )
;
