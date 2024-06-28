import tkinter
# Importing everything from tkinter
from tkinter import *
from tkinter.messagebox import showerror
import math
# Creating the functions
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')


def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')


# Creating a GUI
root = Tk()
root.title("CALCULATOR")
root.geometry('1000x700')
root.resizable(10, 100)
root.configure(background='#a6d1d2',borderwidth=3,)

# StringVar variables
entry_strvar = StringVar(root)

# Defining the top
Label(root, text='CALCULATOR', font=('Cambria', 32,"bold"),bg='lavender', fg='#535798',borderwidth=3,relief=RIDGE ).place(x=370, y=17)

Label(root, text='Press \'x\' twice for exponentiation', font=("Comic Sans MS", 13), bg='lavender',fg='#414141',borderwidth=3,relief=RIDGE ).place(x=365, y=75)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=25, font=12, state='disabled',borderwidth=3,relief=RIDGE)
eqn_entry.place(x=367, y=108)

# Number Buttons
Button(root, height=2, width=5, text='7', font=9, bg='White', command=lambda: add_text("7", entry_strvar)).place(x=370, y=206)

Button(root, height=2, width=5, text='8', font=9, bg='white', command=lambda: add_text('8', entry_strvar)).place(x=439, y=206)

Button(root, height=2, width=5, text='9', font=9, bg='White', command=lambda: add_text('9', entry_strvar)).place(x=508, y=206)

Button(root, height=2, width=5, text='4', font=9, bg='White', command=lambda: add_text('4', entry_strvar)).place(x=370, y=272)

Button(root, height=2, width=5, text='5', font=9, bg='White', command=lambda: add_text('5', entry_strvar)).place(x=439, y=272)

Button(root, height=2, width=5, text='6', font=9, bg='White', command=lambda: add_text('6', entry_strvar)).place(x=508, y=272)

Button(root, height=2, width=5, text='1', font=9, bg='White', command=lambda: add_text('1', entry_strvar)).place(x=370, y=338)

Button(root, height=2, width=5, text='2', font=9, bg='White', command=lambda: add_text('2', entry_strvar)).place(x=439, y=338)

Button(root, height=2, width=5, text='3', font=9, bg='White', command=lambda: add_text('3', entry_strvar)).place(x=508, y=338)

Button(root, height=2, width=5, text='0', font=9, bg='White', command=lambda: add_text('0', entry_strvar)).place(x=370, y=404)

# Operator Buttons

π = math.pi
pi = Button(root, height=2, width=5, text='π', font=9, bg='lightsteelblue3', command=lambda: add_text('π', entry_strvar))
pi.place(x=576, y=473)

subtract = Button(root, height=2, width=5, text='-', font=9, bg='lightsteelblue3', command=lambda: add_text('-', entry_strvar))
subtract.place(x=576, y=338)

multiply = Button(root, height=2, width=5, text='x', font=9, bg='lightsteelblue3', command=lambda: add_text('*', entry_strvar))
multiply.place(x=576, y=272)

divide = Button(root, height=2, width=5, text='/', bg='lightsteelblue3', font=9, command=lambda: add_text('/', entry_strvar))
divide.place(x=576, y=206)

decimal = Button(root, height=2, width=5, text='.', font=9, bg='white', command=lambda: add_text('.', entry_strvar))
decimal.place(x=439, y=404)

perc = Button(root, height=2, width=5, text='%', font=9, bg='lightsteelblue3', command=lambda: add_text('%', entry_strvar))
perc.place(x=508, y=404)

add = Button(root, height=2, width=5, text='+', font=9, bg='lightsteelblue3', command=lambda: add_text('+', entry_strvar))
add.place(x=576, y=404)

bracket_open = Button(root, height=2, width=5, text='(', font=9, bg='lightsteelblue3', command=lambda: add_text('(', entry_strvar))
bracket_open.place(x=439, y=140)

bracket_close = Button(root, height=2, width=5, text=')', font=9, bg='lightsteelblue3', command=lambda: add_text(')', entry_strvar))
bracket_close.place(x=508, y=140)

# Equal, C and AC buttons
equal = Button(root, height=2, width=5, text='=', font=9, bg='#205b7a', command=lambda: submit(eqn_entry, entry_strvar))
equal.place(x=508, y=473)

clear = Button(root, height=2, width=5, text='Clear', font=9, bg='#205b7a',command=lambda: entry_strvar.set(entry_strvar.get()[:-1]))
clear.place(x=576, y=140)

AC_btn = Button(root, height=2, width=5, text='AC', font=9, bg='#205b7a', command=lambda: entry_strvar.set(''))
AC_btn.place(x=370, y=140)

# Ok Button
ok_btn = Button(root, height=2, width=11, text='Ok', font=10, bg='#205b7a', command=lambda: root.destroy())
ok_btn.place(x=370, y=473)

# Updating root
root.update()
root.mainloop()