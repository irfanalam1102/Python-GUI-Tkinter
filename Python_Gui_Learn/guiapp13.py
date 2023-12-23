import tkinter

root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Hello\nIndia",height=4)
lbl1.config(width=30,relief="solid",borderwidth=3,anchor="sw",fg="blue")
lbl1.pack()
root.geometry("600x200")
lbl1['fg']='green'
root.mainloop()

