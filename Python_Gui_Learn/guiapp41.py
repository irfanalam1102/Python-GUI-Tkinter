from tkinter import *
root = Tk()
l1=Label(root, text="First Name")
l2=Label(root, text="Last Name")
e1 = Entry(root)
e2 = Entry(root)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.mainloop( )





