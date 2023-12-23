from tkinter import *
def changecolor(e):
   if(e.char=='r'):
       root.config(bg="red")
   elif(e.char=="g"):
       root.config(bg="green")
   elif(e.char=="b"):
        root.config(bg="blue")

root = Tk()
root.geometry('200x200')
root.bind("<Key>",changecolor)
root.mainloop()




