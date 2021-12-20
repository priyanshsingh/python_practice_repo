from tkinter import *

priyansh_root = Tk()

# "WidthxHeight" --> for geometry function of the class Tk
priyansh_root.geometry("640x480")

# width, height --> minsize function
priyansh_root.minsize(320, 240)

# width, height --> maxsize function
priyansh_root.maxsize(900, 720)

varun = Label(text="Hello, this is the first label of my first GUI Window using Tkinter")
varun.pack()
priyansh_root.mainloop()