# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *
 

def sel():
   selection = "You selected the option " + str(v.get())
   label.config(text = selection)

# Creating master Tkinter window
master = Tk()
master.geometry("175x175")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Dictionary to create multiple buttons
values = {"Option 1" : "1",
          "Option 2" : "2",
          "Option 3" : "3"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
                value = value, command = sel).pack(side = TOP, ipady = 5)
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())

label = Label(master)
label.pack()
mainloop()