from tkinter import *
from PIL import Image, ImageTk

main_root = Tk()

main_root.geometry("640x480")
#using PhotoImage from the tkinter package
#photo = PhotoImage(file="image3.png")


#using Image and ImageTk from the PIL package
image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)

photo_label = Label(image=photo)
photo_label.pack()

main_root.mainloop()
