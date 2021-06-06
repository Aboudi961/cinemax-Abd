-- sQLite

DROP TABLE IF EXISTS bestellingen;
DROP TABLE IF EXISTS vertoningen;
DROP TABLE IF EXISTS films;

CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titel TEXT not NULL,
    duur INTEGER NOT NULL,
    IMDB_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS vertoningen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tijdstip TEXT NOT NULL,
    zaalnummer INTEGER NOT NULL,
    drie_D TEXT NOT NULL,
    film_id INTEGER,
    FOREIGN KEY (film_id) REFERENCES films (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS bestellingen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aantal_kind INTEGER NOT NULL,
    aantal_volwassen INTEGER NOT NULL,
    totaalprijs REAL NOT NULL,
    vertoning_id INTEGER,
    FOREIGN KEY (vertoning_id) REFERENCES vertoningen (id) ON DELETE SET NULL
    );
    