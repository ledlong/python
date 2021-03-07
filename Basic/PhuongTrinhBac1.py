from tkinter import *

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    if a == 0:
        if b == 0:
            stringKQ.set("Vô số nghiệm")
        else:
            stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x = {0}".format(str(-b/a)))

root = Tk()
root.title("Phương trình bậc nhất")
root.resizable(width=True, height=True)
root.minsize(width=250,height=130)
Label(root,text="Phương trình bậc nhất", foreground = 'red',font=("tohama",16), justify = CENTER).grid(row=0,columnspan=2)
stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()
Label(root,text="Hệ số a: ").grid(row=1,column=0)
Entry(root,width=30,textvariable = stringHSA).grid(row=1,column=1)
Label(root,text="Hệ số b: ").grid(row=2,column=0)
Entry(root,width=30,textvariable = stringHSB).grid(row=2,column=1)
frameButton = Frame()
Button(frameButton,text="Giải",command = giaiAction).pack(side=LEFT)
Button(frameButton,text="Tiếp",command = tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoát",command = root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)
Label(root,text="Kết quả",justify=CENTER).grid(row=4,column=0)
Entry(root,width=30,textvariable = stringKQ).grid(row=4,column=1)
root.mainloop()

