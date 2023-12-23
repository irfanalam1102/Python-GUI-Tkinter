import tkinter

root=tkinter.Tk()
root.title("My GUI App")
strObj=tkinter.StringVar()
lbl1=tkinter.Label(root,borderwidth=2,relief="solid",textvariable=strObj)
lbl1.pack()
strObj.set("Python Is Fun!!")
root.geometry("600x200")
root.mainloop()

