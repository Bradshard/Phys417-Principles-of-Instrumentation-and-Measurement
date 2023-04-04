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

def money_scale():
    message = "M"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode()+message_2.encode())

def more_precise_Weight_Scale():
    message = "MWS"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode()+message_2.encode())

def Weight_Scale():
    message = "WS"
    message_2 = "\r\n"
    arduino.write(message.encode()+message_2.encode())
    print(message.encode()+message_2.encode())



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
    command=money_scale)

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
    command = Weight_Scale)

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
    command = more_precise_Weight_Scale)

button_3.grid(
    row=3,
    columnspan=2,
    sticky='n',
    ipadx=5,
    ipady=5
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