from ansimarkup import ansiprint as print
from utils.terminalultils import toon_menu
from models.vertoningen import Vertoning
from datetime import datetime
import os
from db.datamanager import Datamanager
from prettytable import PrettyTable
from utils.terminalultils import clear_terminal, print_waarschuwing, toon_menu

def beheer_vertoningen():
    dm = Datamanager
    menu_items = [
        "lijst alle vertoningen",
        "vertoningen toevoegen",
        "vertoningen verwijderen"
    ]

    while True:
        clear_terminal()
        print("<black,green> BEHEER VERTONING </black,green>")
        keuze = toon_menu(menu_items)

        if keuze == 0 :
            break

        if keuze == 1 :
            vertoningen = dm.alle_vertoningen([])
            tabel = PrettyTable()
            tabel.field_names = [
                "tijdstip" "zaalnummer" "drie_D" "film_id"
            ]
            
            tabel.add_row([[vertoning.tijdstip, vertoning.zaalnummer, vertoning.drie_D, vertoning.film_id] for vertoning in vertoningen])
            print(tabel)