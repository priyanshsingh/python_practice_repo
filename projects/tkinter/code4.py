from tkinter import *

root = Tk()
root.geometry("1380x340")
root.title("Hello World Title")

# Important Lable options

# text = adds text
# bd = background
# fg = foregrounf
# font = sets the font
#                 font=("times new roman", 14, "bold", "italic")
#                 font="times new roman 14 bold italic"
# padx = padding in x
# pady = padding in y
# relief = style of border(SUNKER, RAISED, GROOVE, RIDGE)

title_label = Label(text='''Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes 
code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help 
programmers write clear, logical code for small and large-scale projects.

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), 
object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as 
Python 0.9.0.[34] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage 
collection system (in addition to reference counting). Python 3.0 was released in 2008 and was a major revision of the language that is not 
completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.''', bg="red", fg = "white", padx=20, pady=40, 
font=("verdana", 12, "bold", "italic"), borderwidth=3, relief=SUNKEN)

# Important PACK options
# Anchor = nw

title_label.pack(anchor="ne")

root.mainloop()