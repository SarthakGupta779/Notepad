from tkinter.filedialog import *
import tkinter as tk
from tkinter import Frame, BOTH, LEFT, WORD, END, INSERT
from tkinter import Button
from tkinter import Entry


def savefile():
    new_file = asksaveasfile(mode='w', filetype=[('text file', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()


def openfile():
    file = askopenfile(mode='r', filetype=[('text file', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)


def clearfile():
    entry.delete(1.0, END)


canvas = tk.Tk()
canvas.geometry("400x700")
canvas.title("Notepad")
canvas.config(bg = "white")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = Button(canvas, text="open", bg = "white", command = openfile)
b1.pack(in_ = top, side = LEFT)
b2 = Button(canvas, text="save", bg = "white",command = savefile)
b2.pack(in_ = top, side = LEFT)
b3 = Button(canvas, text="clear", bg = "white",command = clearfile)
b3.pack(in_ = top, side = LEFT)
b4 = Button(canvas, text="exit", bg = "white", command = exit)
b4.pack(in_ = top, side = LEFT)
entry = tk.Text(canvas, bg ="grey", font = ("poppins", 16))
entry.pack(padx =10, pady = 5, expand = True, fill = BOTH)
canvas.mainloop()