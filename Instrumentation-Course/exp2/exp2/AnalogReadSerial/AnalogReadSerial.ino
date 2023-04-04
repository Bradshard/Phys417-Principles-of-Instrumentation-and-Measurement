const int analogPin = A0;


void setup() {
  Serial.begin(9600);
}
void loop() {
  int analogValue = analogRead(analogPin);
  float val = analogValue * (5.0 / 1023.0);
Serial.println(val);

  delay(1);        // delay in between reads for stability
}
