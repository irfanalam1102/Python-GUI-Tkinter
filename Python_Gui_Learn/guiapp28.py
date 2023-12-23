
from tkinter import *
def showMessage():
   l1.config(text="Welcome To Python")

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me",command=showMessage)
l1=Label(root)
b1.pack()
l1.pack()
root.mainloop()


