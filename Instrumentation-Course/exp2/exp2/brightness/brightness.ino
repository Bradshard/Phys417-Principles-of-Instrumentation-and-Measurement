const int analogPin = A0; 
//It makes behavior of the analogpin as constant.
const int ledPin = 9;
void setup() {
  //It set up Arduino to run.
  pinMode(ledPin,OUTPUT); 
  // It set the specified pin as a INPUT or OUTPUT.
  Serial.begin(9600);
  // It adjusts rate of data in bits per second for transmission.
}

void loop() { 
  // It makes our operations to run again and again.
  int analogValue = analogRead(analogPin);
  // It reads analogPin as an analog input. "int" means integer. "analogValue" is a thing we determined.
  int brightness = map(analogValue, 0, 1023, 0 ,255);
  // I determined the range of brightness 0 to 255 by using map function.
  //0-255 corresponds to %100 duty cyle.
  analogWrite(ledPin,brightness);
  //It writes analog value to ledPin.It is based on the PWM technique which is used for getting analog results from digital sources.
  delay(1);
  // It pauses the program for specified time.
}
