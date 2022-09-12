#!/dev/usr/python3

import serial # Importerar bilioteket för seriellkommunikation.

while 1:
   ser = serial.Serial('/dev/ttyACM0', 9600) # Lagrar datan i variabeln var.
   readText = ser.readline()   # Readline läser ut och lagrar sista raden och skriver denna till variabeln readText.
   print (readText)            # skriver ut datat hos variabeln readtext.

