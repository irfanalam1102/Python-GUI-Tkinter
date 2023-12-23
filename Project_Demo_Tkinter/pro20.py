import tkinter
import sys
def show():
   f_name= e1.get()
   L_name=e2.get()
   l3.config(text=f_name+" "+L_name)
def finish():
    sys.exit()
root=tkinter.Tk()
root.geometry("200x200")
l1=tkinter.Label(root,text="F_name")
l2=tkinter.Label(root,text="L_name")
l3=tkinter.Label(root,width=20,anchor='w',font="Arial 10 bold")
e1=tkinter.Entry(root)
e2=tkinter.Entry(root)
b1=tkinter.Button(root,text="Show",command=show)
b2=tkinter.Button(root,text="quit",command=finish)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=1,columnspan=2,sticky='W')
b1.grid(row=3,column=1,sticky='W',pady=4)
b2.grid(row=3,column=1)
root.mainloop()