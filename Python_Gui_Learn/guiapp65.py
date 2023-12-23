import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

button_tk = tk.Button(root, text="tkinter Button")
button_ttk = ttk.Button(root, text="ttk Button")

button_tk.pack(padx=10, pady=10)
button_ttk.pack(padx=10, pady=10)

root.mainloop()
