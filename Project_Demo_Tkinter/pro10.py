import tkinter
root=tkinter.Tk()
root.geometry("600x400")
l1=tkinter.Label(root,text="Hello\nindia",font="arial 22 bold",borderwidth=4,relief="solid",bg="blue",fg="white")
l2=tkinter.Label(root,text="i love python\nprograming",font="arial 16 bold",borderwidth=6,relief="solid",bg="green",fg='red')
l1.pack()
l2.pack()
root.mainloop()