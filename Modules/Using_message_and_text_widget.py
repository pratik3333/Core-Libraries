#Program to show use of Text and Message widget
#Importing module and creating window
from tkinter import *
start=Tk()

#Using Text Widget
start.title("Using Text and message Widget")
text1=Text(height=10,width=70,bg="pink")
text1.insert(END,"Hello and welcomee to the world of \nGraphical User Interface in python using tkinter module.\nThis module has many widgets.")
text1.pack()

#Using Message widget
message1=Message(text="Happy Learning")
message1.pack()

#Displaying the result
start.mainloop()