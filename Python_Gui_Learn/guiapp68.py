import tkinter
class MyGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("My GUI App")
        self.root.geometry("600x300+500+400")
        self.lb1=tkinter.Label(self.root,text="Welcome To GUI")
        self.btn = tkinter.Button(self.root, text="Click For Message",command=self.show)
        self.lb1.pack()
        self.btn.pack()
    def show(self):
        self.lb1.config(text="Welcome To Python")


root=tkinter.Tk()
obj=MyGUI(root)
root.mainloop()

