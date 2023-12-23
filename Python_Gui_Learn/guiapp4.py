import tkinter
root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Welcome To Python",bg="red",fg="blue")
lbl1.pack()
root.config(bg="yellow")
root.geometry("600x200")
root.mainloop()

