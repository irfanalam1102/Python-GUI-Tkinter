from tkinter import *
from tkinter import colorchooser, messagebox

def showopen():
 chosen_color=colorchooser.askcolor(color="#0000ff",title="Select your fav color")
 if chosen_color[0] is None:
     messagebox.showinfo("Your selection","No color chosen")
 else:
     root.config(bg=chosen_color[1])


root = Tk()
root.geometry("200x200")
btn=Button(root,text="Choose Color",command=showopen)
btn.pack()
root.mainloop()
