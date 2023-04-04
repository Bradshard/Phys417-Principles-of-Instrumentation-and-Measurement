#include "max6675.h"
int ktcSO = 8; // Output pin that carries each bit "serial open"
int ktcCS = 9; // Input pin that tells the Arduino board that it is time for the thermocouple to read and send the data "Chip Select"
int ktcCLK = 10; // Pin that indicates when a new data bit is entered "Clock" indicates in which intervals the clock is going to work.



MAX6675 ktc(ktcSO, ktcCS, ktcCLK);

void setup() {
  Serial.begin(9600);
  // give the Max a little time to settle
  delay(500);
}


void loop() {
  float sensorValue = analogRead(A5);
  float kelvin = (ktc.readCelsius() +273.15);
  Serial.print("T(kelvin) = ");
  Serial.print(kelvin);
  Serial.print("\t");
  Serial.print("Thermistor Value = ");
  Serial.println(sensorValue);
  digitalWrite(12,HIGH);
  delay(500);
}
