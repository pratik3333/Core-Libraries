#Program to show the use of Checkbutton widget
#Importing module and creating window.
from tkinter import *
third=Tk()
third.title("Using checkbox")
#Creating lable and arranging on window.
lable1=Label(third,text="select your hobbies")
lable1.pack()

#creating check boxes.
check1=Checkbutton(third,text="Swimming",width=20,height=2,bg="red",fg="blue")
check2=Checkbutton(third,text="Reading",width=20,height=2,bg="red",fg="blue")
check3=Checkbutton(third,text="Driving",width=20,height=2,bg="red",fg="blue")
check4=Checkbutton(third,text="Playing Cricket",width=20,height=2,bg="red",fg="blue")

#Arranging check boxes on window.
check1.pack()
check2.pack()
check3.pack()
check4.pack()

#Displaying the result
third.mainloop()