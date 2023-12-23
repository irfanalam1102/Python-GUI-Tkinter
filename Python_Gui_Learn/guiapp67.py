import tkinter
class MyGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("My GUI App")
        self.root.geometry("600x300+500+400")
        self.lb1=tkinter.Label(self.root,text="Welcome To GUI")
        self.lb1.pack()
    def show(self):
        pass


root=tkinter.Tk()
obj=MyGUI(root)
root.mainloop()

