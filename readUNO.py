#!/usr/bin/python3

import time
import serial

windPrint = ""
windSpeed = 999

while 1:
   ser = serial.Serial('/dev/ttyACM0', 9600)
   windPrint = ser.read().decode('ascii')
   tempfil = open('/sys/bus/w1/devices/28-0000095c963e/temperature')
   temperatur = tempfil.read()
   windPrint = windPrint.replace('\n','').replace('\r','')

   if windPrint.isnumeric():
      windSpeed = int(windPrint)

   if windSpeed < 999:
      if len(temperatur) > 0:
         temperaturprint = (float(temperatur) / 1000)
         temperaturprint = str(temperaturprint)
         print(f'\rTemperaturen är: {temperaturprint[:4]} C och Vindhastigheten är: {windSpeed} m/s     ', end='')
      time.sleep(0.15)
      tempfil.close()
   elif windSpeed == 999:
      print('---Awaiting a valid wind speed value.---\n')
      time.sleep(1)
