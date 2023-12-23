import tkinter
root=tkinter.Tk()
root.geometry("600x400")
l1=tkinter.Label(root,text="process finished with exit code 0")
l1.config(font="arial 22 bold",borderwidth=4,relief="solid",bg='green',fg='red',height=12,anchor='n')
l1.pack()
root.mainloop()