import tkinter
import datetime
root=tkinter.Tk()
root.title("my first application")
root.geometry("500x500")
def timetable():
    a=datetime.datetime.now()
    print(a)
t1=tkinter.Label(root,text="clik hare")
b1=tkinter.Button(root)
