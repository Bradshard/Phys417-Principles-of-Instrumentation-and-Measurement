int count = 0;                                                           // sets button count to 0
const byte interruptPin = 2;   
// defines 3rd pin as interrupt
void setup() {
  pinMode(interruptPin, INPUT_PULLUP);                                   // configure interruptPin as an input and enable the internal pull-up resistor
  attachInterrupt(digitalPinToInterrupt(interruptPin), flag, RISING);    // when the button is pressed, it sends voltage through the digital pin,
                                                                         // interrupting the loop, raises a flag when its interrupted
  Serial.begin(9600);                                                    // opens serial port for monitoring, sets data rate to 9600
}
void loop() {
  Serial.println(count);                                                 // Prints count as  a line, meaning, moves to a new data each print
}
void flag() {                                                            // aforementioned flag
  count++;                                                               // increases the flag count by one each time it was raised
}
