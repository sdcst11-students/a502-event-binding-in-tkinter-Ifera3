"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *
from math import *

window = tk.Tk()
window.title('Factoring')

b1pm = StringVar()
b1pm.set('+')
b2pm = StringVar()
b2pm.set('+')

l1 = Label(window, text='x^2')
b1 = Button(window, textvariable=b1pm)
eb = Entry(window, width=2)
l2 = Label(window, text='x')
b2 = Button(window, textvariable=b2pm)
ec = Entry(window, width=2)
b3 = Button(window, text='factor')
efactor = Entry(window)

def b1swap(event):
    print(event)

    if b1pm.get() == '+':
        b1pm.set('-')
    elif b1pm.get() == '-':
        b1pm.set('+')

def b2swap(event):
    print(event)

    if b2pm.get() == '+':
        b2pm.set('-')
    elif b2pm.get() == '-':
        b2pm.set('+')

def factor(event):
    print(event)

    try:
        if b1pm.get() == '-':
            b = 0 - int(eb.get())
        else:
            b = int(eb.get())
        if b2pm.get() == '-':
            c = 0 - int(ec.get())
        else:
            c = int(ec.get())
        x1 = round(-(-b + sqrt((b**2) - (4 * c)))/2,2)
        x2 = round(-(-b - sqrt((b**2) - (4 * c)))/2,2)
        if x1 < 0:
            bracket1 = f'(x - {abs(x1)})'
        else:
            bracket1 = f'(x + {x1})'
        if x2 < 0:
            bracket2 = f'(x - {abs(x2)})'
        else:
            bracket2 = f'(x + {x2})'
        efactor.delete(0,END)
        efactor.insert(0, f'{bracket1}{bracket2}')
    except:
        efactor.delete(0,END)
        efactor.insert(0, 'Fail')
        print('fail')

b1.bind('<Button>', b1swap)
b2.bind('<Button>', b2swap)
b3.bind('<Button>', factor)

l1.grid(row=1, column=1)
b1.grid(row=1, column=2, padx=3)
eb.grid(row=1, column=3)
l2.grid(row=1, column=4)
b2.grid(row=1, column=5, padx=3)
ec.grid(row=1, column=6)
b3.grid(row=1, column=7, padx=3)
efactor.grid(row=1, column=8)

window.mainloop()