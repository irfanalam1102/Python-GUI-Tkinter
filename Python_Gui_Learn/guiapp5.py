import tkinter
root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Welcome To Python")
lbl1.config(font="arial 22 italic")
lbl1.pack()
root.geometry("600x200")
root.mainloop()

