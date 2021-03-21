from tkinter import *
from playsound import playsound


def btnClick(number):
    global operator
    playsound("tit.wav", block=True)
    operator = operator + str(number)
    text_input.set(operator)


def btlClearScreen():
    global operator
    operator = ""
    text_input.set("")


def btnEqualInput():
    global operator
    sumInput = str(eval(operator))
    text_input.set(sumInput)


cal = Tk()
cal.title("Calculator")
operator = ""
text_input = StringVar()

txtDisplay = Entry(cal, textvariable=text_input, font=("arial", 20, 'bold'), bd=30,
                   insertwidth=4, bg="powder blue", justify="right").grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="7",
              bg="powder blue", command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="8",
              bg="powder blue", command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="9",
              bg="powder blue", command=lambda: btnClick(9)).grid(row=1, column=2)
addition = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+",
                  bg="powder blue", command=lambda: btnClick('+')).grid(row=1, column=3)
# ----------------------------------------------------------------------------------------------------------------------
btn4 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="4",
              bg="powder blue", command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="5",
              bg="powder blue", command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="6",
              bg="powder blue", command=lambda: btnClick(6)).grid(row=2, column=2)
subtraction = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-",
                     bg="powder blue", command=lambda: btnClick("-")).grid(row=2, column=3)
# ----------------------------------------------------------------------------------------------------------------------
btn1 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="1",
              bg="powder blue", command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="2",
              bg="powder blue", command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="3",
              bg="powder blue", command=lambda: btnClick(3)).grid(row=3, column=2)
multiplication = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="x",
                        bg="powder blue", command=lambda: btnClick("*")).grid(row=3, column=3)
# ----------------------------------------------------------------------------------------------------------------------
btn0 = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="0",
              bg="powder blue", command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="C",
                  bg="powder blue", command=btlClearScreen).grid(row=4, column=1)
btnEqual = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="=",
                  bg="powder blue", command=btnEqualInput).grid(row=4, column=2)
division = Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="/",
                  bg="powder blue", command=lambda: btnClick('/')).grid(row=4, column=3)

cal.mainloop()
