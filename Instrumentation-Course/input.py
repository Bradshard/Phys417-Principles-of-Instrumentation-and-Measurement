import serial
import time

arduino = serial.Serial('COM3', 9600)

def onOffFunction():
    command = input("Type something: (on/ off / bye )")
    if command == "on":
     print ("The LED is on")
     time.sleep(1)
     arduino.write('H'.encode())
     onOffFunction()
    elif command == "off":
        print("The LED is off")
        time.sleep(1)
        arduino.write('L'.encode())
        onOffFunction()
    elif command == "bye":
        print("See You!")
        time.sleep(1)
        arduino.close()
    else:
        print ("Sorry, not a command!")
        onOffFunction()

        time.sleep(2)

onOffFunction()