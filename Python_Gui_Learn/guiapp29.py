
from tkinter import *
import datetime
def showDateTime():
  obj=datetime.datetime.now()
  str=obj.strftime("%d-%B-%Y %I:%M:%S %p")
  l1.config(text=str)

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me",command=showDateTime)
l1=Label(root)
b1.pack()
l1.pack()
root.mainloop()


