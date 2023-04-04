int count = 0;                                                           
// It starts to count from 0.
const byte interruptPin = 3;   
//When we click to button, we interrupt the program. To interrupt the program, we defined the pin 2 as an interruptPin.
void setup() {
    //It set up Arduino to run.
  pinMode(interruptPin, INPUT_PULLUP);
  //If we write only "INPUT", pin listens whatever voltage is connected to pin.
  //If we write INPUT_PULLUP,the pin is connected to internalpullup resistor. Hence we can read better readings.
  attachInterrupt(digitalPinToInterrupt(interruptPin), flag, RISING);    
  // It determines a interrupt number. When we interrupt, the voltage comes from digital pin. 
  // "Flag" let the program know there happens a interrupt.
  // There will be interrupt when signal goes from LOW to HIGH.
  Serial.begin(9600);    
    // It adjusts rate of data in bits per second for transmission. 
}
void loop() {
    //It makes our operations to run again and again.
  Serial.println(count);                                              
    // It prints the values on serial port screen, so we can see it.
}
void flag() {                                                            
  // It provides to use flag.
  count++;                                                              
  // It increases when the flag increases
}
