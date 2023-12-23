from tkinter import *

def changecolor():
   if obj.get()==1:
       root.config(bg="#ff0000")
   else:
       root.config(bg=old_color)

root = Tk()
root.geometry("200x200")
old_color=root["bg"]
obj=IntVar()
cb=Checkbutton(root,text="Red",command=changecolor,variable=obj)
cb.pack()
root.mainloop()
