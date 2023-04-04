const int analog_Pin = A1;


void setup() {
  Serial.begin(9600);
}
void loop() {
  int analog_Value = analogRead(analog_Pin);
  float val = analog_Value * (5.0 / 1023.0);
  int val2 = map(analog_Value, 0, 1023, 0, 5);
Serial.println(val2);

  delay(100);        // delay in between reads for stability
}