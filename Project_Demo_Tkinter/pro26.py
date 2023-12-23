import tkinter
from tkinter import ttk

def show():
    f_name=e1.get()
    l_name=e2.get()
    l3.config(text=f_name +" "+l_name)

def quitt():
    root.destroy()




root=tkinter.Tk()
root.geometry('300x300')
l1=ttk.Label(root,text="F name")
l2=ttk.Label(root,text="L name")
l3=tkinter.Label(root,width=20,anchor='w',font="Arial 10 bold")
e1=ttk.Entry(root)
e2=ttk.Entry(root)
b1=ttk.Button(root,text="show",command=show)
b2=ttk.Button(root,text='Quit',command=quitt)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=1)
b1.grid(row=3,column=1)
b2.grid(row=3,column=2)
root.mainloop()