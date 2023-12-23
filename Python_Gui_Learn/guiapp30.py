
from tkinter import *
count=0
def incrementCount():
   global count
   count=count+1
   l1.config(text=str(count))


root=Tk()
root.geometry("200x200")
b1=Button(root,text="Click Me",command=incrementCount)
l1=Label(root,text="0")
b1.pack()
l1.pack()
root.mainloop()
