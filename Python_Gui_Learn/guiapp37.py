from tkinter import *

root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me")
b1.bind("<Button-1>",lambda e: root.config(bg="red"))
b1.bind("<Button-3>",lambda e: root.config(bg="blue"))
b1.pack()
root.mainloop()

