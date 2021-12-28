from tkinter import *
from PIL import Image, ImageTk

main_root = Tk()
image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo)
photo_label.pack()



main_root.mainloop()