from tkinter import *
def leftClick(e):
    root.config(bg="red")
def rightClick(e):
    root.config(bg="blue")
root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me")
b1.bind("<Button-1>",leftClick)
b1.bind("<Button-3>",rightClick)
b1.pack()
root.mainloop()

