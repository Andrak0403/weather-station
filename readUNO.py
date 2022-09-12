#!/dev/usr/python3

import serial

while 1:
   ser = serial.Serial('/dev/ttyACM0', 9600)
   readText = ser.readline()
   print (readText)

