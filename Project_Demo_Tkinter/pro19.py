import tkinter
import sys
def show():
   fname= e1.get()
   lname= e2.get()
   l3.config(text=fname+" "+lname)
def finish():
    sys.exit(0)

root=tkinter.Tk()
root.geometry("300x300")
l1=tkinter.Label(root,text="first name")
l2=tkinter.Label(root,text="last name")
l3=tkinter.Label(root,width=4,font="Arial 10 bold")
e1=tkinter.Entry(root)
e2=tkinter.Entry(root)
b1=tkinter.Button(root,text="show",command=show)
b2=tkinter.Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,columnspan=2)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1.grid(row=3,column=0,pady=4)
b2.grid(row=3,column=1,pady=4)
root.mainloop()
