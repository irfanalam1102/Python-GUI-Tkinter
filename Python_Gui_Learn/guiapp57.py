from tkinter import *
from tkinter import messagebox

def showgender():
 data=x.get()
 if data==1:
    messagebox.showinfo("Your selection","You selected Male")
 else:
    messagebox.showinfo("Your selection", "You selected Female")

root = Tk()
root.geometry("200x200")
x=IntVar()
l1=Label(root,text="Select your gender")
rb1=Radiobutton(root,text="Male",command=showgender,variable=x,value=1)
rb2=Radiobutton(root,text="Female",command=showgender,variable=x,value=2)

l1.grid(row=0,column=0)
rb1.grid(row=1,column=0,sticky=W)
rb2.grid(row=2,column=0,sticky=W)

root.mainloop()
