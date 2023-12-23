import tkinter
root=tkinter.Tk()
root.geometry("600x200")
l1=tkinter.Label(root,text="Indian flag ")
l1.config(font="arial 22 bold",borderwidth=4,relief='solid',bg='green',fg='red')
l1.pack()
root.mainloop()