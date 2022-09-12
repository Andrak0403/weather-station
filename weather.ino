/*
  Analog Input

  Demonstrates analog input by reading an analog sensor on analog pin 0 and
  turning on and off a light emitting diode(LED) connected to digital pin 13.
  The amount of time the LED will be on and off depends on the value obtained
  by analogRead().

  The circuit:
  - potentiometer
    center pin of the potentiometer to the analog input 0
    one side pin (either one) to ground
    the other side pin to +5V
  - LED
    anode (long leg) attached to digital output 13 through 220 ohm resistor
    cathode (short leg) attached to ground

  - Note: because most Arduinos have a built-in LED attached to pin 13 on the
    board, the LED is optional.

  created by David Cuartielles
  modified 30 Aug 2011
  By Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInput
*/

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 8;      // select the pin for the LED
uint16_t sensorValue = 0;  // variable to store the value coming from the sensor
uint8_t windData = 0;
float outputWindData = 0.0;
uint16_t sensorData = 0;


void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);

  //Seriekommunikation för väderdata. TEMPORÄR FÖR ATT SENARE ANPASSAS.
  Serial.begin(9600);
  
}

void loop() {
  // read the value from the sensor: ANEMOMETERN
  sensorData = analogRead(sensorPin);
  sensorValue = constrain(sensorData, 200, 750);
    
  float windData = map(sensorValue, 200, 750, 0, 342);
  float outputWindData = float(windData/10);
  digitalWrite(ledPin,HIGH);
  Serial.print(outputWindData);
  Serial.println(" m/S");
  delay(125);
  digitalWrite(ledPin,LOW);
  delay(125);
}
