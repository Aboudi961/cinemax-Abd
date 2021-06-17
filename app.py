from adminapp.beheer_films import beheer_films
from adminapp.beheer_vertoningen import beheer_vertoningen
from adminapp.beheer_bestellingen import beheer_bestellingen
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
from utils.terminalultils import invoer_getal, toon_menu
from utils.terminalultils import clear_terminal, invoer_getal, toon_menu


menu_items = [
    "Beheer films",
    "Beheer vertoningen",
    "Beheer bestellingen" 
]
while True:
    clear_terminal()

    print ("<white,blue>  CINEMAX  </white,blue>")
    keuze = toon_menu(menu_items, "Afsluiten")

    if keuze == 0:
        break
    if keuze == 1:
        beheer_films()
    if keuze == 2:
        beheer_vertoningen()
    if keuze == 3:
        beheer_bestellingen()