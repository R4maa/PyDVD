from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors

for m in get_monitors():
    print(str(m))


root = Tk()
root.title("DvD")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.geometry('+200+100')

root.mainloop()
