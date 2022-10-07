#!/usr/bin/python3

import time
import serial


windPrint = ""
windSpeed = 999
ser = serial.Serial('/dev/ttyACM0', 9600)
s = [0]

while 1:
   #windPrint = ser.readline()
   #print(windPrint)
   ser = serial.Serial('/dev/ttyACM0', 9600)
   windPrint = ser.readline().decode('ascii')
   #print(windPrint)
   tempfil = open('/sys/bus/w1/devices/28-0000095c963e/temperature')
   temperatur = tempfil.read()
   windPrint = windPrint.replace('\n','').replace('\r','')
   # print(windPrint)

   if windPrint.isnumeric():
      windSpeed = int(windPrint)
      windSpeed = windSpeed / 10

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
