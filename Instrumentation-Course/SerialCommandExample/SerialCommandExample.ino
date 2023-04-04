// Demo Code for SerialCommand Library
// Steven Cogswell
// May 2011

#include <SerialCommand.h>

#define arduinoLED 9   // Arduino LED on board
#define input_1 5
#define input_2 6
#define enb 11 

SerialCommand sCmd;     // The demo SerialCommand object

void setup() {
  pinMode(arduinoLED, OUTPUT);      // Configure the onboard LED for output
  digitalWrite(arduinoLED, LOW);    // default to LED off

  Serial.begin(9600);

  // Setup callbacks for SerialCommand commands
  sCmd.addCommand("ON",    LED_on);          // Turns LED on
  sCmd.addCommand("OFF",   LED_off);         // Turns LED off
  sCmd.addCommand("HELLO", sayHello);        // Echos the string argument back
  sCmd.addCommand("P",     processCommand);  // Converts two arguments to integers and echos them back
  sCmd.addCommand("R",     right);
  sCmd.addCommand("L",     left);
  sCmd.setDefaultHandler(unrecognized);      // Handler for command that isn't matched  (says "What?")
  Serial.println("Ready");
}

void loop() {
  sCmd.readSerial();     // We don't do much, just process serial commands
}


void LED_on() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  aNumber = atoi(arg); 
  Serial.println("LED on");
  digitalWrite(arduinoLED, HIGH);
}

void right() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  aNumber = atoi(arg); 
  Serial.println("yes");
  digitalWrite(input_1, HIGH);
  digitalWrite(input_2, LOW);
}

void left() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  aNumber = atoi(arg); 
  Serial.println("yes");
  digitalWrite(input_2, HIGH);
  digitalWrite(input_1, LOW);
}

void LED_off() {
  int aNumber;
  char *arg;
  arg = sCmd.next();
  aNumber = atoi(arg); 
  Serial.println("LED off");
  digitalWrite(arduinoLED, LOW);
}

void sayHello() {
  char *arg;
  arg = sCmd.next();    // Get the next argument from the SerialCommand object buffer
  if (arg != NULL) {    // As long as it existed, take it
    Serial.print("Hello ");
    Serial.println(arg);
  }
  else {
    Serial.println("Hello, whoever you are");
  }
}


void processCommand() {
  int aNumber;
  char *arg;

  Serial.println("We're in processCommand");
  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atoi(arg);    // Converts a char string to an integer
    Serial.print("First argument was: ");
    Serial.println(aNumber);
    analogWrite(arduinoLED,aNumber);
    analogWrite(enb,aNumber);
  }
  else {
    Serial.println("No arguments");
  }

  arg = sCmd.next();
  if (arg != NULL) {
    aNumber = atol(arg);
    Serial.print("Second argument was: ");
    Serial.println(aNumber);
    analogWrite(arduinoLED,aNumber);
    analogWrite(enb,aNumber);
  }
  else {
    Serial.println("No second argument");
  }
}

// This gets set as the default handler, and gets called when no other command matches.
void unrecognized(const char *command) {
  Serial.println("What?");
}
