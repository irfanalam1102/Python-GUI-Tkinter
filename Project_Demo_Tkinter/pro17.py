import tkinter
def clic():
    l1=tkinter.Label(root,text="i love python")
    l1.pack()

root=tkinter.Tk()
root.geometry("600x200")
root.title("my GUI ")
b1=tkinter.Button(root,text="click me",command=clic)
b1.pack()
root.mainloop()