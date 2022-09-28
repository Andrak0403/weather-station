/*******************************************************
 *Större förändringar: Rensat upp kommenterade 
 * funktioner och tagit bort onödiga beräkningar.
 * 
 ******************************************************/

int sensorPin = A0;           // select the input pin for the potentiometer
uint16_t sensorValue = 0;     // variable to store the value coming from the sensor
uint16_t windData = 0;        // Variabel för datautskrift till RPi.
//float outputWindData = 0.0; // Variabel för flyttal vilka skickades tidigare till RPi.
uint16_t sensorData = 0;      // Variabel för rådata från nånting jag inte minns.


void setup() {
  // declare the ledPin as an OUTPUT:
//   pinMode(ledPin, OUTPUT);

  //Seriekommunikation för väderdata. TEMPORÄR FÖR ATT SENARE ANPASSAS.
  Serial.begin(9600);
  
}

void loop() {
  /***********************************************
   *ANEMOMETERN
   * Analog avläsning av analog pin A0.
   * mappning utav analogt värde vilket
   * konverteras till ett 16bits heltal (<350)
   * Man skulle kunna använt ett uint8 i stället
   * men då hade andra tal krävts.
   **********************************************/
  sensorData = analogRead(sensorPin);
  sensorValue = constrain(sensorData, 60, 450);

   windData = map(sensorValue, 81, 400, 0, 324); //Tog bort float 
  //float outputWindData = float(windData/10);
  
  /*************************************************
   * Datatransmission!
   ************************************************/
  Serial.println(windData); // SÄNDER ENBART RÅDATA
  delay(50);
  /*************************************************
   * Datatransmission stop!
   ************************************************/
}
