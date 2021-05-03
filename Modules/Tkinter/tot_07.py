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
<<<<<<< HEAD:Modules/Tkinter/tot_07.py

lable1.pack(side="left",anchor="sw",fill="y")
root.mainloop()
=======
lable1.pack(side="right",anchor="se",fill="y")
root.mainloop()
>>>>>>> be0db87d6c1c9fe40e104eccf47d8069d4e78f88:Modules/tot_07.py
