from pyfirmata2 import Arduino, util
import time
from LCD import LCD


# Vervang 'COM5' door de poort die je Arduino gebruik
board = Arduino('COM3')
board.samplingOn(180)
lcd = LCD(board)

lcd.clear()
lcd.print("Hello World!")
lcd.set_cursor(0, 1)
lcd.print("123")
while True:
    time.sleep(1)
