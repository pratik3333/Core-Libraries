from tkinter import *
def getvals():
    print(namevalue.get())
    print(agevalue.get())
    print(mobilenumbervalue.get())
    print(cityvalue.get())
root=Tk()
root.geometry("633x433")
root.title("DanceClass Form")

name = Label(root,text="Name")
age = Label(root,text="Age")
mobilenumber = Label(root,text="MobileNumber")
city = Label(root,text="City")
name.grid(row=0,column=1)
age.grid(row=1,column=1)
mobilenumber.grid(row=2,column=1)
city.grid(row=3,column=1)

namevalue=StringVar()
agevalue=StringVar()
mobilenumbervalue=StringVar()
cityvalue=StringVar()

nameentry=Entry(root,textvariable=namevalue)
ageentry=Entry(root,textvariable=agevalue)
mobilenumberentry=Entry(root,textvariable=mobilenumbervalue)
cityentry=Entry(root,textvariable=cityvalue)

nameentry.grid(row=0,column=2)
ageentry.grid(row=1,column=2)
mobilenumberentry.grid(row=2,column=2)
cityentry.grid(row=3,column=2)

Button(text="Submit",command=getvals).grid()
root.mainloop()