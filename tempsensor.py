#!/usr/bin/python3

import time 
while True:
    tempfil = open('/sys/bus/w1/devices/28-0000095c963e/temperature')
    temperatur = tempfil.read()
    temperaturprint = (int(temperatur) / 1000)
    temperaturprint = str(temperaturprint)
    print(f'Temperaturen ar {temperaturprint [:4]} C') 
    time.sleep(0.5)
    tempfil.close()
