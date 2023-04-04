void setup() { 
  //It set up Arduino to run.

  Serial.begin(9600); 
  // It adjusts rate of data in bits per second for transmission.
}

void loop() { 
  //It makes our operations to run again and again.

  int sensorValue = analogRead(A0); 
  //It reads A0 as an analog input. "int" means integer. "sensorvalue" is a thing we determined.
  int newvalue = map(sensorValue,0,1023,0,5);
  //I determined a newvalue and I used map function to adjust numbers to a new range.
  delay(1);       
  // It pauses the program for specified time.
    Serial.println(newvalue); 
  // It prints the values on serial port screen, so we can see it.
}
