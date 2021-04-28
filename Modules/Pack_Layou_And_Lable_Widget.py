#Program for using lable widget in pack layout
#importing module and creating window.
from tkinter import *
root = Tk()
lable1=Label(text="Infosys",bg="red",height=5,width=100)
lable2=Label(text="Hindustan Level Ltd.",bg="yellow",height=5,width=100)
lable3=Label(text="Tata Consultancy Service",bg="green",height=5,width=100)
lable4=Label(text="Accenture",bg="blue",height=5,width=100)

lable1.pack()
lable2.pack()
lable3.pack()
lable4.pack()
root.mainloop()