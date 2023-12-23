import tkinter
root = tkinter.Tk()
root.geometry('200x200+100+200')
l1=tkinter.Label(root,text="Name:")
l2=tkinter.Label(root,text="Password:")
e1=tkinter.Entry(root)
e2=tkinter.Entry(root,show="*")
b1=tkinter.Button(root,text="Login")
b2=tkinter.Button(root,text="Quit")
l1.grid(row=0,column=0,sticky=tkinter.E)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
root.mainloop()


