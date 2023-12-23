from tkinter import *

def changecolor():
   root.config(bg=obj.get())

root = Tk()
root.geometry("200x200")
old_color=root["bg"]
obj=StringVar()
cb=Checkbutton(root,text="Red",command=changecolor,variable=obj,onvalue="#ff0000",offvalue=old_color)
cb.deselect()
cb.pack()
root.mainloop()
