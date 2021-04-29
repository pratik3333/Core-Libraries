from tkinter import *
root=Tk()
root.title("TOM")
lable1=Label(text='''From Wikipedia, the free encyclopedia
Jump to navigationJump to search
This article is about the American actor. \nFor other people named Tom Cruise, see Tom Cruise (disambiguation).
Tom Cruise
Tom Cruise by Gage Skidmore 2.jpg
Cruise in 2019
Born	Thomas Cruise Mapother IV
July 3, 1962 (age 58)
Syracuse, New York, U.S.
Occupation	
Tom Cruise signature.svg
Thomas Cruise Mapother IV (born July 3, 1962) is an American actor and producer.''',bg="grey",fg="white",padx=30,pady=30,
        font="comicsansms 10 bold",borderwidth=5,relief=SUNKEN )

lable1.pack()
lable1.pack(side="right",anchor="se",fill="y")
root.mainloop()
