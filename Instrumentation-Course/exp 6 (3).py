from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def show_msg():
   messagebox.showinfo("Message", frm.winfo_children())


tkWindow = Tk() 
frm = Frame(tkWindow) 
tkWindow.geometry("175x175")  
tkWindow.title('Gui')


# Dictionary to create multiple buttons
values = {"Option 1" : "Button 1",
          "Option 2" : "Button 2",
          "Option 3" : "Button 3"}


Button_1 = ttk.Button(frm, text= values["Option 1"], command = show_msg).pack()
Button_2 = ttk.Button(frm, text= values["Option 2"], command = show_msg).pack()
Button_3 = ttk.Button(frm, text= values["Option 3"], command = show_msg).pack() 

frm.pack()
  
tkWindow.mainloop()

# couldn't solve message problem.