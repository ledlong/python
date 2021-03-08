"""This program is to update and delete information of students which
are loaded from mysql database named ledongdb"""
from tkinter import *
from tkinter import Listbox
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hoilamgi",
    database="ledongdb"
)
mycursor = mydb.cursor()

def getListBox():
    sqlSelect = "SELECT firstname, lastname, average, datebirth FROM student WHERE id = %s"
    valID = listbox.curselection()
    global val
    val = listbox.get(valID)
    mycursor.execute(sqlSelect,val)
    idStd = mycursor.fetchall()
    strLastName.set(idStd[0][0])
    strFirstName.set(idStd[0][1])
    strAver.set(idStd[0][2])
    strDateBirth.set(idStd[0][3])

def showListBox():
    sql = "SELECT id FROM student"
    mycursor.execute(sql)
    id = mycursor.fetchall()
    for x in id:
        listbox.insert('end', x)

def updateStudent():
    sqlUpdate = "UPDATE student SET lastname=%s,firstname=%s,average=%s WHERE id=%s"
    valUpdate = (str(strLastName.get()),str(strFirstName.get()),float(strAver.get()),val[0])
    mycursor.execute(sqlUpdate, valUpdate)
    mydb.commit()
    messagebox.showinfo("Update Information","Student Information has been updated successfully!")
    strLastName.set("")
    strFirstName.set("")
    strAver.set("")
    strDateBirth.set("")

def delListBox():
    getListBox()
    sqlDelete = "DELETE FROM student WHERE id = %s"
    cond = (val[0],)
    mycursor.execute(sqlDelete, cond)
    ans = messagebox.askyesno("Delete Confirmation", "Are you sure to delete this student from database? This can't be reversed!")
    if ans:
        mydb.commit()
        messagebox.showinfo("Update Information", "Student Information has been deleted successfully!")
        # Delete all elements in listbox and reload it
        listbox.delete(0,'end')
        showListBox()

# This part is to design an interface to edit information of students
form = Tk()
strLastName = StringVar()
strFirstName = StringVar()
strAver = StringVar()
strDateBirth = StringVar()
form.title("Edit Student Information")
form.resizable(height=True,width=True)
form.minsize(height=270,width=220)
Label(form,text="Student ID:").place(x=5,y=5)
frame = Frame()
listbox = Listbox(frame,selectmode=SINGLE,height=5,width=18)
showListBox()
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill = BOTH)
listbox.pack(side=RIGHT, fill = BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)
frame.place(x=80,y=10)
adframe = Frame(form)
Button(adframe,text="Get Information",command=getListBox).pack(side=RIGHT)
Button(adframe,text="Delete Information",command=delListBox).pack(side=RIGHT)
adframe.place(x=5,y=100)
Label(form,text="Last Name:").place(x=5,y=140)
Entry(form,textvariable=strLastName).place(x=80,y=140)
Label(form,text="First Name:").place(x=5,y=160)
Entry(form,textvariable=strFirstName).place(x=80,y=160)
Label(form,text="GPA:").place(x=5,y=180)
Entry(form,textvariable=strAver).place(x=80,y=180)
Label(form,text="Date of Birth:").place(x=5,y=200)
Entry(form,textvariable=strDateBirth).place(x=80,y=200)
Button(form,text="Update Information",command=updateStudent).place(x=80,y=230)
form.mainloop()

