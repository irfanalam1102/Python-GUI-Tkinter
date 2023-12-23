
from tkinter import *
def incrementCount():
   obj.set(obj.get()+1)

root=Tk()
root.geometry("200x200")
b1=Button(root,text="Click Me",command=incrementCount)
obj=IntVar()
l1=Label(root,textvariable=obj)
b1.pack()
l1.pack()
root.mainloop()
