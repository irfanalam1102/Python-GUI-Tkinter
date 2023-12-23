from tkinter import *
root = Tk()
root.geometry("200x200")
lb1=Listbox(root)
sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]

#write your logic to add sport names to ListBox

for s in sports:
    lb1.insert(END,s)


lb1.grid(row=1,column=0,sticky=W)
print("total sports:",lb1.size())
root.mainloop()
