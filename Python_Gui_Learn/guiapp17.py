import tkinter

root=tkinter.Tk()
root.title("My GUI App")
intObj=tkinter.IntVar()
lbl1=tkinter.Label(root,borderwidth=2,relief="solid",textvariable=intObj)
lbl1.pack()
intObj.set(125)
root.geometry("600x200")
root.mainloop()

