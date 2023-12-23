from tkinter import *
def enterKey(e):
    root.config(bg="Red")
def escapeKey(e):
    root.config(bg=oldColor)
root = Tk()
root.geometry('200x200')
oldColor=root["bg"]
root.bind("<Return>",enterKey)
root.bind("<Escape>",escapeKey)
root.mainloop()


