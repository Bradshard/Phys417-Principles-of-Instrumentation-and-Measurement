import time
import serial
import matplotlib.pyplot as plt
from drawnow import *

f = open("volt_time.txt", "x")
"""
def makeFig():                                              # Create a function that makes our desired plot
    plt.ylim(0, 100)                                        # Set y limit as 0 to 500
    plt.xlabel('Time')
    plt.title('Volts vs time')                         # Write the title
    plt.grid(True)                                          # Turn the grid on
    plt.ylabel('Volts')                                # Set y's label
    plt.plot(value_array, 'ro-', label='Volts')     # plot the resistance
    plt.legend(loc='lower left')                            # plot the legend
"""
cout = 0
cout_as_array =[]
value_array = []
ser = serial.Serial('COM3', 9600) 
 
while True: 
    value = ser.readline().decode().strip("\r\n") 
    print(value)
    f.write(value)

    time.sleep(0.1) 
    value_array.append(value)
    cout_as_array.append(cout)
    cout += 1
    #drawnow(makeFig)   
    if (cout == 51):
        f.close()
        break 
"""
plt.plot(cout_as_array,value_array, color= "orange")
plt.title("Value vs cout")
plt.ylabel("Value in Volts")
plt.xlabel("Count as cout")

plt.gcf().savefig("Volts vs count.pdf")
"""