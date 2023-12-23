import tkinter
root=tkinter.Tk()
l1=tkinter.Label(root,text="Name")
l2=tkinter.Label(root,text="Password",)
e1=tkinter.Entry(root)
e2=tkinter.Entry(root,show="*")
b1=tkinter.Button(root,text="Login")
b2=tkinter.Button(root,text="Quit")
c1=tkinter.Checkbutton(root,text="keep me login")
l1.grid(row=0,column=0,sticky=tkinter.E)
e1.grid(row=0,column=1,columnspan=2)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1,columnspan=2)
c1.grid(row=2,column=0,columnspan=2)
b1.grid(row=3,column=1)
b2.grid(row=3,column=2)
root.mainloop()


