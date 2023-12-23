import tkinter
import tkinter.font as tkfont
root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Welcome To Python")
myFont=tkfont.Font(weight="bold",size=24)
lbl1.config(font=myFont)
lbl1.pack()
root.geometry("600x200")
root.mainloop()

