#program to show use of Button widget
#importing module and creating window
from tkinter import *
second=Tk()

second.title("Using lable and Button")

#Creating a frame
frame1=Frame(second,height=100,width=500,bg="blue")
frame1.pack()

#Creating a button and adding it the window.
lable1=Label(second,text="Select one option")
lable1.pack()

#Creating Button and adding it the window
button1=Button(second,text="OK",width=20,height=5,bg="red",fg="blue")
button2=Button(second,text="Cancel",width=20,height=5,bg="red",fg="blue")
button1.pack()
button2.pack()


#Displaying the result
second.mainloop()