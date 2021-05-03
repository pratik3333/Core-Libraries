from tkinter import *
root = Tk()
root.geometry("633x433")
root.title("Packing Buttons in TKinter")
def hello():
    print("Hello Tkinter buttons")

def name():
    print("PRATIK")

def age():
    print("21")

frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side="left",anchor="nw")

b1=Button(frame,text="print now",fg="red",command=hello)
b1.pack(side="left",padx=20)

b2=Button(frame,text="Name",fg="red",command=name)
b2.pack(side="left",padx=20)

b3=Button(frame,text="Age",fg="red",command=age)
b3.pack(side="left",padx=20)

b4=Button(frame,text="print now",fg="red")
b4.pack(side="left",padx=20)

root.mainloop()