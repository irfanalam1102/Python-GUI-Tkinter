from tkinter import *
def show(val):
    x=int(val)
    red=hex(x)
    red=red[2:]
    print(red)
    if len(red)==1:
        red="0"+red;
    root.config(bg="#"+red+"0000")
root=Tk()
root.geometry('300x300')
sc=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=show)
sc.pack()
root.configure(bg="#000000")
root.mainloop()