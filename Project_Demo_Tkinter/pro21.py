import tkinter
def devide():
    try:
        c.set("")
        e3.config(fg="red")
        c.set(a.get()/b.get())
        e3.config(fg="green")
    except ZeroDivisionError:
        c.set("cann't devide by zero")
    except ValueError:
        c.set("only digit allow")
def show():
 a.set("")
 b.set("")
 c.set("")
 e1.focus()
def finish():
    root.destroy()
root=tkinter.Tk()
root.geometry("400x200+100+100")
a=tkinter.IntVar()
b=tkinter.IntVar()
c=tkinter.IntVar()
a.set("")
b.set("")
c.set("")
l1=tkinter.Label(root,text="Number of Devision",width=20,anchor='w',font="Arial 10 bold")
l2=tkinter.Label(root,text="Enter first number")
l3=tkinter.Label(root,text="Enter second number")
l4=tkinter.Label(root,text="Result")
e1=tkinter.Entry(root,textvariable=a)
e2=tkinter.Entry(root,textvariable=b)
e3=tkinter.Entry(root,textvariable=c)
b1=tkinter.Button(root,text="Devide",command=devide)
b2=tkinter.Button(root,text="clear",command=show)
b3=tkinter.Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0)
e1.grid(row=1,column=1)
l2.grid(row=1,column=0)
e2.grid(row=2,column=1)
l3.grid(row=2,column=0,sticky='e')
l4.grid(row=3,column=0,sticky='e')
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,sticky='e',pady=5,padx=5)
b2.grid(row=4,column=1,pady=5,padx=5,sticky='e')
b3.grid(row=4,column=2,pady=5,padx=5,sticky='w')
root.mainloop()


