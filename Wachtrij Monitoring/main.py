import pyfirmata2
import time
import json
from LCD import LCD

# Laad de configuratie
try:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("config.json bestand niet gevonden!")
    exit()

board = pyfirmata2.Arduino('COM3')
board.samplingOn(300)
lcd = LCD(board)

# Definieer de pinnen voor de sensoren
detection_pin_add = board.get_pin('d:2:u')
detection_pin_min = board.get_pin('d:3:u')

inkomende_bezoekers = config["inkomende_bezoekers"]
verwerkings_snelheid = config["verwerkings_snelheid"]
min_personen_wachtrij = config["min_personen_wachtrij"]
gem_personen_wachtrij = config["gem_personen_wachtrij"]
max_personen_wachtrij = config["max_personen_wachtrij"]


def add_callback(released):
    global inkomende_bezoekers
    if not released:
        if inkomende_bezoekers < max_personen_wachtrij:
            inkomende_bezoekers += 1
            print(f"Personen erin: {inkomende_bezoekers}")
        else:
            print("Maximum aantal bereikt, kan niemand meer naar binnen.")


def min_callback(released):
    global inkomende_bezoekers
    if not released:
        if inkomende_bezoekers > min_personen_wachtrij:
            inkomende_bezoekers -= 1
            print(f"Personen eruit: {inkomende_bezoekers}")
        else:
            print("Er zijn geen mensen om eruit te laten.")


def check_count():
    global inkomende_bezoekers
    print(f"Controleren aantal bezoekers: {inkomende_bezoekers}")  # Debugging
    if inkomende_bezoekers == min_personen_wachtrij:
        board.digital[13].write(0)
        board.digital[12].write(0)
        board.digital[11].write(1)  # Groen
        print('Led wordt groen')
    elif inkomende_bezoekers > gem_personen_wachtrij:
        board.digital[13].write(0)
        board.digital[12].write(1)  # Geel
        board.digital[11].write(0)
        print('Led wordt geel')
    elif inkomende_bezoekers == max_personen_wachtrij:
        board.digital[13].write(1)  # Rood
        board.digital[12].write(0)
        board.digital[11].write(0)
        print('Led wordt rood')


def display():
    global inkomende_bezoekers, verwerkings_snelheid
    wachttijd = round(inkomende_bezoekers / verwerkings_snelheid, 2)
    print(f"Bereken wachttijd: {wachttijd} minuten")  # Debugging

    lcd.clear()
    lcd.set_cursor(0, 1)
    lcd.print(f"Wachttijd: {wachttijd} min")

    print(f"Gemiddelde wachttijd: {wachttijd} minuten")


# Registreer de callbacks
detection_pin_add.register_callback(add_callback)
detection_pin_min.register_callback(min_callback)

try:
    print("*Begin checken van bezoekersaantal.*j")
    check_count()
    while True:
        time.sleep(3)
        display()
except KeyboardInterrupt:
    print('Programma gestopt door gebruiker.')
    lcd.clear()
finally:
    board.exit()
    print("Verbinding gestopt")
