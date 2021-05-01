#program to show of Frame and Entry Widget
#Importing module and creating window with title
from tkinter import *
first=Tk()
first.title("My First Frame")

#Creating a frame and specifying its dimensions.
frame1=Frame(height=100,width=500,bg="blue")
frame1.pack()

#Creating a lable and adding it to window
lable=Label(text="Enter your name:")
lable.pack()

#Creating an entry box and adding it to window
entry1=Entry()
entry1.pack()

#Creating a lable and entry box and adding them to window
lable1=Label(text="Enter your city")
lable1.pack()
entry2=Entry()
entry2.pack()

#Displaying the result
first.mainloop()