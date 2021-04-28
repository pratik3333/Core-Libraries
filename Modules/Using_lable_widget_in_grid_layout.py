#program for using lable widget in grid layout
#Importing module and creating window.
from tkinter import *
root=Tk()

#Adding Lables in thr Grid layout
lable1=Label(text="Infosys",bg="red",height=5,width=50)
lable2=Label(text="Hindustan Level Ltd.",bg="yellow",height=5,width=50)
lable3=Label(text="Tata Consultancy Services",bg="green",height=5,width=50)
lable4=Label(text="Accenture",bg="blue",height=5,width=50)

lable1.grid(row=0,column=0)
lable2.grid(row=0,column=1)
lable3.grid(row=1,column=0)
lable4.grid(row=1,column=1)

#Displaying the result
root.mainloop()