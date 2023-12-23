from tkinter import *
from tkinter.font import *
root=Tk()
myfont=Font(weight="bold")
l1=Label(root,text="user name ")
l2=Label(root,text="password",font=myfont)
b1=Button(root)
b2=Button(root)
e1=Entry(root)
e2=Entry(root)
l2.pack()
e2.pack(root)
root.mainloop()

