int sensorPin = A0;    // select the input pin for the potentiometer
//int ledPin = 13;      // select the pin for the LED
int powerPin = 13;

int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  pinMode(powerPin, OUTPUT);
  digitalWrite(powerPin, LOW);
  // declare the ledPin as an OUTPUT:
  //pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}
void loop() {
  delay(58000);
  digitalWrite(powerPin, HIGH);
  delay(2000);
  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
  digitalWrite(powerPin, LOW);
  
  
  // read the value from the sensor:
  //sensorValue = analogRead(sensorPin);
  //Serial.println(sensorValue);
  /*
  if (sensorValue < 700) {
    Serial.println("*UNKO*");
  } else {
    Serial.println("*AHO*");
  }
  */
  
  /*
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(5000);  
  */
  
}
