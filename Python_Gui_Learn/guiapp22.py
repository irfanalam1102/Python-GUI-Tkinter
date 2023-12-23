import tkinter
root = tkinter.Tk()
l1=tkinter.Label(root, text="Red Sun", bg="red", fg="white")
l2=tkinter.Label(root, text="Green Grass", bg="green", fg="black")
l3=tkinter.Label(root, text="Blue Sky", bg="blue", fg="white")
l1.pack(padx=(50,0))
l2.pack(padx=(0,50))
l3.pack(padx=50)
root.mainloop()

