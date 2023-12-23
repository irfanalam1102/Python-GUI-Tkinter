import tkinter
root=tkinter.Tk()
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
width=screenwidth//2
height=screenheight//2
xco=screenwidth//4
yco=screenheight//4
root.geometry("600x400")
root.resizable(False,False)
root.mainloop()