from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.title("A Digital Clock")
root.resizable(height=False, width=False)
root.configure(background="black")

def dateDisplay():
    stringDate = time.strftime("%d:%b:%Y")
    labelDate.configure(text=stringDate)
    labelDate.after(1000, dateDisplay)

def timeDisplay():
    stringTime = time.strftime("%H:%M:%S %p")
    labelTime.configure(text=stringTime)
    labelTime.after(1000, timeDisplay)

labelDate = Label(root, font=("ds-digital", 100), background="black", foreground="cyan")
labelDate.pack(anchor="center")
labelTime = Label(root, font=("ds-digital", 100), background="black", foreground="cyan")
labelTime.pack(anchor="center")
try:
    dateDisplay()
    timeDisplay()
    mainloop()
except:
    print(dateDisplay())
