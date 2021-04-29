#program for creating a canvas
#Importing module and creating window.
from tkinter import *
mycanvas=Tk()

mycanvas.title("My First Canvas")
canvas1=Canvas(width=300,height=300)

#Creating a line with the specified two points
canvas1.create_line(5,25,250,25)

#Creating an oval with the specified points
canvas1.create_oval(250,250,50,100,fill="red")

#creating a rectangle with the specified points
canvas1.create_rectangle(30,30,50,60,fill="green")

#creating a polygon with the specified points
canvas1.create_polygon(57,60,150,90,178,90,200,150,300,250,fill="blue")

#Using pack layout for display of canvas
canvas1.pack()

#Displaying the result
mycanvas.mainloop()