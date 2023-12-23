from tkinter import *
from tkinter import filedialog, messagebox
def showopen():
 file_names=filedialog.askopenfilenames(initialdir="e:/",title="Select your fav songs",filetypes=[("mp3 files","*.mp3")])
 str=""
 if type(file_names) is tuple:
    for file in file_names:
      str+=file+"\n"
    lbl.config(text=str)
 else:
   messagebox.showinfo("Your selection","no file selected")

root = Tk()
root.geometry("600x300")
btn=Button(root,text="Open Files",command=showopen)
lbl=Label(root,text="Your selected file names will appear here")
btn.pack()
lbl.pack()
root.mainloop()
