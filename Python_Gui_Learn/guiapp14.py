import tkinter

root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root)
myimg=tkinter.PhotoImage(file="d:/images/login_icon_1.gif")
lbl1.config(image=myimg)
lbl1.pack()
root.geometry("600x200")
root.mainloop()

