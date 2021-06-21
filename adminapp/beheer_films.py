from models.films import Film
from ansimarkup import ansiprint as print
from utils.terminalultils import clear_terminal, print_fout, print_instructie, print_waarschuwing, toon_menu
from db.datamanager import Datamanager
from prettytable import PrettyTable
import os
def beheer_films():
    dm = Datamanager()
    menu_items = [
        "lijst alle films",
        "film toevoegen",
        "film verwijderen",
        "film zoeken"
    ]

    while True:
        clear_terminal()
        print("<black,green> BEHEER FILMS </black,green>")
        keuze = toon_menu(menu_items)
        tabel = PrettyTable()

        if keuze == 0:
            break

        if keuze == 1:
            films = dm.alle_films()
            
            tabel.field_names = ["titel", "duur", "IMDB_id"]
            
            tabel.add_rows([[film.titel, film.duur, film.IMDB_id] for film in films])
            print(tabel)
            nieuwe_film = Film(titel, duur, IMDB_id)
            dm.film_toevoegen(nieuwe_film)

        if keuze == 2:
            while True:
                
                
                print_waarschuwing("wil je een film toevoegen j/n")
                answer = input()
                if answer == "j":
                    titel = input("Geef de titel van de film: ")
                else:
                    break
                duur = int(input("Hoeveel lang de film die je wilt toevoegen "))
                if duur == int:
                    continue
                else:
                    break
                
            while True:
                tabel = PrettyTable()
                IMDB_id = input("Voeg de film code toe ")
                if IMDB_id[0:2] == "tt":
                    break

            tabel.field_names = [
                "id", "titel", "duur", "IMDB_id"
            ]

            tabel.add_row([titel, duur, IMDB_id])
            print(tabel)
            tabel = Film(titel, duur, IMDB_id)      

            
            if keuze == 3:
                film_delet = input("Geef film IMDB_id te verwijderen ")
                while True:
                    film = dm.film_verwijderen_imdb(film_delet)
                    if film:
                        tabel = PrettyTable()
                        
                        
                        film_delet = input("Geef film IMDB_id te verwijderen ")
                        tabel.field_names = ["titel", "duur", "IMDB_id" ]
                        tabel.add_row([film_delet.title, film_delet.duur, film_delet.IMDB_id])
                        print(tabel)
                        break
                    else:
                        ValueError

    print("<i>Druk op enter om verder te geen</i>")
    input()