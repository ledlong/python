# This program is to add more student into the database named ledongdb
import mysql.connector
from tkinter import messagebox
from tkinter import *
# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hoilamgi",
    database="ledongdb"
)
mycursor = mydb.cursor()
def insertStudent():
    if (len(strID.get())==0) or (len(strLastName.get())==0) or (len(strFirstName.get())==0) \
            or (len(strAver.get())==0) or (len(strDateBirth.get())==0):
        messagebox.showwarning("Warning", "Some fields cannot be left blank!")
    else:
        sqlcom = "INSERT INTO student (id,firstname,lastname,average,datebirth) VALUES (%s,%s,%s,%s,%s)"
        val = (strID.get(),strLastName.get(),strFirstName.get(),strAver.get(),strDateBirth.get())
        mycursor.execute(sqlcom,val)
        mydb.commit()
        messagebox.showinfo("Information", "Inserted successfully!")
    ans = messagebox.askyesno("Continue","Do you want to continue?")
    if ans == True:
        strID.set("")
        strLastName.set("")
        strFirstName.set("")
        strAver.set("")
        strDateBirth.set("")
    else:
        strID.set("")
        strLastName.set("")
        strFirstName.set("")
        strAver.set("")
        strDateBirth.set("")
        exit()

# Design the form to input data into the database
form = Tk()
form.title("Student Management")
form.resizable(height=True, width=True)
form.minsize(height=140,width=205)
strID = StringVar()
strLastName = StringVar()
strFirstName = StringVar()
strAver = StringVar()
strDateBirth = StringVar()
Label(form, text="Student ID:").grid(row=0,column=0)
Entry(form,textvariable=strID).grid(row=0,column=1)
Label(form,text="Last Name:").grid(row=1,column=0)
Entry(form,textvariable=strLastName).grid(row=1,column=1)
Label(form, text="First Name:").grid(row=2,column=0)
Entry(form,textvariable=strFirstName).grid(row=2,column=1)
Label(form,text="GPA:").grid(row=3,column=0)
Entry(form,textvariable=strAver).grid(row=3,column=1)
Label(form,text="Date of Birth:").grid(row=4,column=0)
Entry(form,textvariable=strDateBirth).grid(row=4,column=1)
fr = Frame()
Button(fr,text="Cancel",command=form.quit).pack(side=LEFT)
Button(fr,text="Insert",command=insertStudent).pack(side=LEFT)
fr.grid(row=5,columnspan=2)
form.mainloop()