
from tkinter import *
def showMessage():
    print("Welcome To Python")
root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me",command=showMessage)
b1.pack()
root.mainloop()


