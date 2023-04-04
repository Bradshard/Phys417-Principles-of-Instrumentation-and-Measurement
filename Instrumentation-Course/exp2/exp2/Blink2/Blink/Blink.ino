void setup() { // It set up Arduino to run. We make basic settings such as determining which pin 
               //will be used for what or determining the transmission speed of data. 
              //These code is runned for one time when the program starts running.
pinMode(LED_BUILTIN, OUTPUT); // It set the specified pin as a INPUT or OUTPUT.
}
void loop() { // It makes our operations to run again and again.
  digitalWrite(LED_BUILTIN, HIGH);  // It used to determine state of the digital pins. 
                                    //They can be OUTPUT and write or send data to our device. 
                                    //Also they can be INPUT and take or read data from components.
                                    
                                    // Arduino UNO has a LED and resistor which are connected
                                    // each other on a pin and LED_BUILTIN takes this pin's number.
                                    // This number is 13 in my Arduino.

                                    //I already realized there was a light on Ardunio blinks with the LED at the same time. 
                                    
                                    // HIGH means 5V.
 delay(100);
                                    
  digitalWrite(LED_BUILTIN, LOW); // LOW means 0V.
 delay(100);                      // It pauses the program for specified time.
}
