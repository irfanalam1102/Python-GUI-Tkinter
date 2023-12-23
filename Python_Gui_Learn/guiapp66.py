import tkinter
class MyGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("My GUI App")
        self.root.geometry("600x300+500+400")
    def show(self):
        pass


root=tkinter.Tk()
obj=MyGUI(root)
root.mainloop()

