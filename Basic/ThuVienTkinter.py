from tkinter import *

root = Tk()
root.title("This is a window")
root.resizable(width=True,height=True)
# root.minsize(width=400,height=300)
# root.maxsize(width=600,height=500)

Label(root,text='Hello, this is the first window',justify=CENTER,relief=SUNKEN).pack(pady=10)
Label(root,text='My name is Long Le',foreground='red',background='black',justify=LEFT,relief=FLAT).pack(side=LEFT,padx=5)
Label(root,text='I am a graduate student',justify=RIGHT,relief=GROOVE).pack(side=RIGHT,pady=10)
Button(root,text='Yes',command=root.quit).pack(side=RIGHT)
Button(root,text='No').pack(side=RIGHT)
Label(root,text='Insert your name: ',justify=CENTER,relief=FLAT).pack(padx=5, side=LEFT)
name = StringVar()
Entry(root,textvariable=name,width=60).pack(side=LEFT)
name.set("Put your name here")
root.mainloop()