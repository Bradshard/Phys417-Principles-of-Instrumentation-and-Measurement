import tkinter as tk
from tkinter import ttk
import serial
import time

# root window
root = tk.Tk()
root.geometry('350x275')
root.resizable(False, False)
root.title('Precision Scale GUI')

# arduino
#arduino = serial.Serial('COM4', 9600) 

#columnconfig
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value = tk.DoubleVar()



def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())

def led_on():
    message = "ON"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode()+message_2.encode())

def led_off():
    message = "OFF"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode()+message_2.encode())

def send_pwm():
    messg = "P "
    message = str(current_value.get())
    message_2 = "\r\n"
    arduino.write(messg.encode()+message.encode() + message_2.encode())
    print(messg.encode()+message.encode() + message_2.encode())

def right():
    message = "R"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode() + message_2.encode())

def left():
    message = "L"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode() + message_2.encode())

"""
# label for the slider
slider_label = ttk.Label(
    root,
    text='PWM:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = tk.Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=0,
    sticky='we'
)
"""

# Button 1
button_1 = ttk.Button(
    root,
    text='Money Scale',
    command=send_pwm)

button_1.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=5,
    ipady=5
)

# Button 2
button_2 = ttk.Button(
    root,
    text='Weight Scale .2',
    command = led_on)

button_2.grid(
    row=2,
    columnspan=2,
    sticky='n',
    ipadx=5,
    ipady=5
)

# Button 3
button_3 = ttk.Button(
    root,
    text='Weight Scale .3',
    command = led_off)

button_3.grid(
    row=3,
    columnspan=2,
    sticky='n',
    ipadx=5,
    ipady=5
)


# current value label
current_value_label = ttk.Label(
    root,
    text='PWM Value:'
)

current_value_label.grid(
    row=6,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=7,
    columnspan=2,
    sticky='n'
)


root.mainloop()