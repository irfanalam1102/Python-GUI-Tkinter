from tkinter import *
def changeColor(e):
    root.config(bg="red")

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me")
b1.bind("<Button>",changeColor)
b1.pack()
root.mainloop()
