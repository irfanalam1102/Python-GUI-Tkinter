import tkinter
root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Welcome To Python")
lbl1.pack()
lbl2=tkinter.Label(root,text="It Is Awesome")
lbl2.pack()
root.geometry("600x400+300+200")
root.mainloop()

