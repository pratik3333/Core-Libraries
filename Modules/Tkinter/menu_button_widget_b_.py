#program to show the use of menu and menu button widget
from tkinter import *
#creating a window and adjusting the size.
fourth=Tk()
fourth.geometry("400x300")
fourth.title("Menu button and Menu widget")

#Creating a menubutton1.
menu1=Menubutton(fourth,text="Countries",relief=RAISED,height=10,width=30,bg="red")
menu1.grid()
menu1.menu=Menu(menu1,tearoff=0)
menu1["menu"]=menu1.menu
In=IntVar()
US=IntVar()
UK=IntVar()
Ch=IntVar()
menu1.menu.add_checkbutton(lable='India',variable=In)
menu1.menu.add_checkbutton(lable='United State',variable=US)
menu1.menu.add_checkbutton(lable='United Kingdom',variaable=UK)
menu1.menu.add_checkbutton(lable='China',variable=Ch)
menu1.grid()
menu1.pack()

#Creating a menubutton2.
menu2=Menubutton(fourth,text="Games",relief=SUNKEN,height=5,width=30,bg="green")
menu2.menu=Menu(menu2,tearoff=0)
menu2["menu"]=menu2.menu
c=IntVar()
h=IntVar()
f=IntVar()
t=IntVar()
menu2.menu.add_checkbutton(lable="Cricket",Variable=c)
menu2.menu.add_checkbutton(lable="Hockey",Variable=h)
menu2.menu.add_checkbutton(lable="Football",Variable=f)
menu2.menu.add_checkbutton(lable="Tennis",Variable=t)
menu2.pack()

#Displaying the result.
fourth.mainloop()
