from tkinter import *
from tkinter import filedialog, messagebox
def showopen():
  file_name=filedialog.askopenfilename(initialdir="d:/",title="Select your fav song",filetypes=[("mp3 files","*.mp3")])
  if file_name!="":
    messagebox.showinfo("Your selection",file_name)
  else:
    messagebox.showinfo("Your selections","No file selected")
root = Tk()
root.geometry("200x200")
btn=Button(root,text="Open File",command=showopen)
btn.pack()
root.mainloop()
