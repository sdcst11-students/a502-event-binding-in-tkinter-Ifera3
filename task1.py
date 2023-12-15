"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title('Info')

l1 = Label(window, text='Name')
l2 = Label(window, text='Student number')
l3 = Label(window, text='Grade')
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
b1 = Button(window, text='=')
e4 = Entry(window, width=40)

def combine(enent):
    print(enent)
    out = 'Name:' + e1.get() + ' Student#:' + e2.get() + ' Grade:' + e3.get()
    e4.delete(0,END)
    e4.insert(0,out)

b1.bind('<Button>',combine)

l1.grid(row=1, column=1)
l2.grid(row=1, column=2)
l3.grid(row=1, column=3)
e1.grid(row=2, column=1)
e2.grid(row=2, column=2)
e3.grid(row=2, column=3)
b1.grid(row=2, column=4)
e4.grid(row=2, column=5)

window.mainloop()