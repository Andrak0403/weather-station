/****************************************************************
 *Analog avläsning av anemommeter för windhastighet, detta sker
 * genom att en spänning genereras när vinden för proppellern
 * att snurra, detta ger en spänning mellan 0,4 till 2,0V
 * vilken senare kvantifiseras till ett 10b tal mellan 0 - 1023.
 * 
 * VÄrdet omräknas sedan till vindhastigeten i m/s med ett tak av 
 * 34,2m/s, alla stora beräkningar görs i heltal.
 * 
 ****************************************************************/




#include "Wire.h"
#include "LiquidCrystal_I2C.h"

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 8;      // select the pin for the LED
uint16_t sensorValue = 0;  // variable to store the value coming from the sensor
uint8_t windData = 0;
float outputWindData = 0.0;
uint16_t sensorData = 0;
//LiquidCrystal_I2C lcd(0x27, 16, 2); //För att skriva ut på LCD.

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);


  //lcd.begin();
  //lcd.backlight();
  //lcd.clear();
  //lcd.setCursor(4,0);
  //lcd.print("Hackster");
  //Seriekommunikation för väderdata. TEMPORÄR FÖR ATT SENARE ANPASSAS.
  Serial.begin(9600);
  
}

void loop() {
  // read the value from the sensor: ANEMOMETERN
  sensorData = analogRead(sensorPin);
  sensorValue = constrain(sensorData, 60, 450);
    
  float windData = map(sensorValue, 81, 400, 0, 324);
  float outputWindData = float(windData/10);
  digitalWrite(ledPin,HIGH);
  Serial.print(outputWindData);
  Serial.println(" m/S");
  delay(55);
}
