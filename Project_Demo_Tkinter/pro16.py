import tkinter
def clic():
    print("i love python")
root=tkinter.Tk()
root.title("my GUI ")
l1=tkinter.Label(root,text="its label")
b1=tkinter.Button(root,text="click me",command=clic)
l1.pack()
b1.pack()
root.mainloop()