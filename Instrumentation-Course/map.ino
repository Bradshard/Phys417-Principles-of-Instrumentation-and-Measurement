void setup() { 
  //It set up Arduino to run.

  Serial.begin(9600); 
  // It adjusts rate of data in bits per second for transmission.
}

void loop() { 
  //It makes our operations to run again and again.

  int val = analogRead(A1); 
  //It reads A1 as an analog input. "int" means integer. 
  int newVal = map(val,0,1023,0,5);
  //I determined a newvalue and I used map function to adjust numbers to a new range.
  delay(100);       
  // It pauses the program for specified time.
    Serial.println(newVal); 
  // It prints the values on serial port screen, so we can see it.
}
