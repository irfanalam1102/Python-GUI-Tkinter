import tkinter
root=tkinter.Tk()
root.title("My GUI App")
img=tkinter.PhotoImage(file="d:/pic" )
root.iconphoto(root,img)
root.geometry("600x300+500+400")
root.resizable(False,False)
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
rootw=sw//2
rooth=sh//2
xco=sw//4
yco=sh//4
root.geometry(f"{rootw}x{rooth}+{xco}+{yco}")
root.mainloop()