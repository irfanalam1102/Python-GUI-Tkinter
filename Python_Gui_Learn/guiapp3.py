import tkinter
root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Welcome To Python")
lbl1.pack()
lbl1.configure(bg="red",fg="white")
root.geometry("600x400+300+200")
root.mainloop()

