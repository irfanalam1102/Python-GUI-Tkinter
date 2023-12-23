import tkinter

root=tkinter.Tk()
root.title("My GUI App")
lbl1=tkinter.Label(root,text="Hello\nIndia",height=4)
lbl1.config(width=30,relief="solid",borderwidth=3,anchor="sw")
lbl1.pack()
root.geometry("600x200")
print(lbl1.keys())
root.mainloop()

