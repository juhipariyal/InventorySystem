from tkinter import *
import sqlite3 as lite

top = Tk('Inventory Managment')
top.geometry('1000x800')


ProductNameL = Label(top, text="Product Name")
ProductName = Entry(top, bd=2)

ProductNameL.grid(row=0, column=0, sticky=W, pady=2)
ProductName.grid(row=0, column=1, sticky=W, pady=2)

QuantityL = Label(top, text="Quantity")
Quantity = Entry(top, bd=5)
QuantityL.grid(row=1, column=0, sticky=W, pady=2)
Quantity.grid(row=1, column=1, sticky=W, pady=2)

Add = Button(top, text="ADD")
Add.grid(row=2, column=0, sticky=W, pady=2)
Remove = Button(top, text="Remove")
Remove.grid(row=2, column=1, sticky=W, pady=2)
Display = Button(top, text="Display")
Display.grid(row=2, column=2, sticky=W, pady=2)

filename = "Inventory.db"


def db_open(filename):
    with lite.connect(filename) as conn:
        print(f"I created my database named {filename}")


db_open("Inventory.db")

top.mainloop()
