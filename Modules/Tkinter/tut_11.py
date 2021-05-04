from tkinter import *

def getvals():
    print("it works: ")
root=Tk()
root.geometry("677x522")
#Heading
Label(root,text="Welcome to harry's Travels",font="comicsansms 13 bold",padx=15,pady=15).grid(row=0,column=3)

#text for form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="EmergencyContact")
paymentmode=Label(root,text="PaymentMode")

#pack text for a form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#Entries for a form
nameentry=Entry(textvariable=namevalue)
phoneentry=Entry(textvariable=phonevalue)
genderentry=Entry(textvariable=gendervalue)
emergencyentry=Entry(textvariable=emergencyvalue)
paymentmodeentry=Entry(textvariable=paymentmodevalue)

#packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#Checkbox and packing it
foodservice=Checkbutton(text="want to prebook your meals?",variable=foodservicevalue,pady=30)
foodservice.grid(row=6,column=3)

#Button & packing it and assigning it a command
Button(text="Submit to harry's Travels",command=getvals).grid(row=7,column=3)
root.mainloop()