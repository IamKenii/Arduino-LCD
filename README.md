Dit is een bijgewerkte versie van de standaardPyfirmata2 ino.

Hier mee kan je een LCD besturen doormiddel van python.

Zie de Main.py voor de code:

Je moet wel het volgende instaleeren via pip:

- pip install pyfirmata2
- pip install pyfirmata


In de Arduino IDE open je -> Tools -> Manage Libraries: 
Zoek naar 'LiquidCrystal_I2C' en installeer de versie van 'Frank de Brabander'

In de arduino IDE open je de .ino die in de StandaardFirmata map staat en upload je deze naar je arduino.

In de main.py staat standaard code om de LCD werkend te krijgen. 

Connection Diagram
- Gnd pin of the LCD to Gnd of the Arduino
- Vcc pin of the LCD to 5V of the Arduino
- SDA pin of the LCD to A4 of the Arduino
- SCL pin of the LCD to A5 of the Arduino
