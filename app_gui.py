from models.films import Film
from models.vertoningen import Vertoning
import PySimpleGUI as gui
from db.datamanager import Datamanager


dm = Datamanager()
films = dm.alle_films()
layout_titel = [gui.Text("cinemax", font="Helvetica 32")]


layout_listbox =[
    gui.Column([
        [gui.Text("Kies een film")],
        [gui.Listbox(values=[], size=(15, 10), key="-FILMS-", enable_events=True)]
    ]),
    gui.Column([
        [gui.Text("vertoningen van de film")],
        [gui.Listbox(values=[], size=(25, 10), key="-VERTONINGEN-", enable_events=True)]
    ])
]

layout_film = [
    gui.Column([
        
    [gui.Text("titel:", size=(10, 1)), gui.Text("", size=(30, 1), key="-titel-")],
    [gui.Text("duur:", size=(10, 1)), gui.Text("", size=(30, 1), key="-duur-")],
    [gui.Text("IMDB_id:", size=(10, 1)), gui.Text("", size=(30, 1), key="-IMDB_id-")]
    
    ])
]

layout_vertoning = [
    gui.Column([
        
    [gui.Text("id:", size=(10, 1)), gui.Text("", size=(30, 1), key="-id-")],
    [gui.Text("tijdstip:", size=(10, 1)), gui.Text("", size=(30, 1), key="-tijdstip-")],
    [gui.Text("zaalnummer:", size=(10, 1)), gui.Text("", size=(30, 1), key="-zaalnummer-")],
    [gui.Text("drie_D:", size=(10, 1)), gui.Text("", size=(30, 1), key="-drie_D-")],
    [gui.Text("film_id:", size=(10, 1)), gui.Text("", size=(30, 1), key="-film_id-")]
    ])
]


layout = [
    layout_titel,
    layout_listbox,
    layout_film,
    layout_vertoning
]

window = gui.Window("Cinemax", layout, size=(640, 480), font="Helvetica 16", element_justification="center")

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    if event == "-FILMS-":
        geselevteerde_film = values["-FILMS-"][0]
        vertoningen = dm.vertoningen_van_film(geselevteerde_film)
        window["-VERTONINGEN-"].update(values=vertoningen)
    if event == "-FILMS-":
        film = values["-FILMS-"][0]

        window["-titel-"].update(value=Film.titel)
        window["-duur-"].update(value=Film.duur)
        window["-IMDB_id-"].update(value=Film.IMDB_id)

    
    if event == "-VERTONINGEN-":
        film = values["-VERTONINGEN-"][1]

        window["-id-"].update(value=Vertoning.id)
        window["-tijdstip-"].update(value=Vertoning.tijdstip)
        window["-zaalnummer-"].update(value=Vertoning.zaalnummer)
        window["-drie_D-"].update(value=Vertoning.drie_D)
        window["-film_id-"].update(value=Vertoning.film_id)
        

window.close()