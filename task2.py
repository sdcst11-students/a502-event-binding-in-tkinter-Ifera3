#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
from tkinter import *
from math import *

window = tk.Tk()
window.title('Pythagous')

la = Label(window, text='a = ')
ea = Entry(window)
lb = Label(window, text='b = ')
eb = Entry(window)
b1 = Button(window, text='c =')
ec = Entry(window)

def pythagousTime(event):
    print(event)

    try:
        a = float(ea.get())
        b = float(eb.get())
        c = sqrt((a**2)+(b**2))
    except:
        c = None
    
    ec.delete(0,END)
    ec.insert(0,round(c,2))

b1.bind('<Button>', pythagousTime)

la.grid(row=1, column=1)
ea.grid(row=1, column=2)
lb.grid(row=1, column=3)
eb.grid(row=1, column=4)
b1.grid(row=1, column=5)
ec.grid(row=1, column=6)

window.mainloop()