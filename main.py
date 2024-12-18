import pyfirmata2

board = pyfirmata2.Arduino('COM3')
board.samplingOn(180)

LCD_PRINT = 0x01
LCD_CLEAR = 0x02
LCD_SET_CURSOR = 0x03

message = "Froggg"

message_bytes = [ord(char) for char in message]
board.send_sysex(LCD_SET_CURSOR, [0, 0])
board.send_sysex(LCD_PRINT, message_bytes)

# Clear the LCD
# arduino.send_sysex(LCD_CLEAR, [])

board.exit()
