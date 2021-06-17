from ansimarkup import ansiprint as print
from utils.terminalultils import clear_terminal, print_waarschuwing, toon_menu
from db.datamanager import Datamanager
from prettytable import PrettyTable
def beheer_films():
    dm = Datamanager
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

        if keuze == 0:
            break
        if keuze == 1:
            films = dm.alle_films([])
            tabel = PrettyTable()
            tabel.field_names = [
                "id", "titel", "duur", "IMDB_id"
            ]
            
            tabel.add_rows([[film.id, film.titel, film.duur, film.IMDB_id] for film in films])
            print(tabel)

        if keuze == 2:
            
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
            
        IMDB_id = input()
        if IMDB_id[0:2] == "tt":
            continue
        else:
            break
           

            

        if keuze == 3:
            pass

        print("<i>Druk op enter om verder te geen</i>")
        input()