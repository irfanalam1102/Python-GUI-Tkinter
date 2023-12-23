import tkinter
import datetime
def clic():
    a=datetime.datetime.now()
    l1=tkinter.Label(root,text=str(a))
    l1.pack()

root=tkinter.Tk()
root.geometry("600x200")
root.title("my GUI ")
b1=tkinter.Button(root,text="click me",command=clic)
b1.pack()
root.mainloop()