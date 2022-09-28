#!/usr/bin/python3

import time
import serial

windPrint = ""
while 1:
   ser = serial.Serial('/dev/ttyACM0', 9600)
   windPrint = ser.read().decode('ascii')
   tempfil = open('/sys/bus/w1/devices/28-0000095c963e/temperature')
   temperatur = tempfil.read()
   windPrint = windPrint.replace(r'\n','')
   if len(temperatur) > 0:
      temperaturprint = (float(temperatur) / 1000)
      temperaturprint = str(temperaturprint)
      print(f'\rTemperaturen är: {temperaturprint[:4]} C och Vindhastigheten är: {windPrint} m/s', end='')
   time.sleep(0.15)
   tempfil.close()
