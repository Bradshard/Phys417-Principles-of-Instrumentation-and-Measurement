void setup() { 
  //It set up Arduino to run.

  Serial.begin(9600); 
  // It adjusts rate of data in bits per second for transmission.
}

void loop() { 
  //It makes our operations to run again and again.

  int sensorValue = analogRead(A0); 
  //It reads A0 as an analog input. "int" means integer. "sensorvalue" is a thing we determined.
  float val = analogValue * (5.0 / 1023.0);
  //float val = analogValue * (5.0 / 1023.0);
  //I determined a val and I made it range 0 to 5.0 so I took float results.
  delay(1);       
        Serial.println(val); 

  // It pauses the program for specified time.

  // It prints the values on serial port screen, so we can see it.
}
