from tkinter import *
root = Tk()
root.geometry('200x200')
root.bind("r",lambda e: root.config(bg="red"))
root.bind("g",lambda e: root.config(bg="green"))
root.bind("b",lambda e: root.config(bg="blue"))
root.mainloop()




