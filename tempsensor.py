#!/usr/bin/python3
#importerar time för att kunna utnyttja en delay
#Programmet läser in  tempsensorns fil i en whle loop och  typecastar till int. 
#Sedan  dividerar detta med tusen för att få tempen i grader
#med detta gjort så  konverteras "temperaturprint" till sträng
#och printas därefter ut  med en formated print för att få en 
#snygg utskrift. När allt är färdigt  körs en delay på 0.5s och filen stängs. 
import time 
while True:
    tempfil = open('/sys/bus/w1/devices/28-0000095c963e/temperature')
    temperatur = tempfil.read()
    temperaturprint = (int(temperatur) / 1000)
    temperaturprint = str(temperaturprint)
    print(f'Temperaturen är {temperaturprint [:4]} C') 
    time.sleep(0.5)
    tempfil.close()
