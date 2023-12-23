import tkinter
import tkinter.font
root=tkinter.Tk()
root.geometry("600x400")
l1=tkinter.Label(root,text="India is leader of G20 for next 5 years")
l1.config(font="areal 28 bold",borderwidth=6,relief="solid",bg='green',fg='red')
l1.pack()
root.mainloop()