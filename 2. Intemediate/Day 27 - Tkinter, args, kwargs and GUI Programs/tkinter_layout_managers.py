from tkinter import *
"""
Tkinter has 3 layout managers: pack, place and grid

pack
----
- Labels will be packed to fit the space by taking center by default, but not expanded to take all space
- very templated, very hard to precisely position items

place
-----
- precise positioning with x and y value, where the top left hand corner is 0, 0 in pixels
- the only downside is that its positioning is so specific

grid
----
- imagines your program is a grid, you can divide it into any number of rows and columns
- you assign row and column numbers and grid arranges everything relative to other positions in the grid

As such, you cannot mix pack and grid in the same program as each arranges its elements relative to other elements in the same program
Only place is individual and counted separately from the other 2 layout managers
"""
window = Tk()
window.title("4x3 grid")
window.minsize(width=400, height=300)

# Add padding around the whole window
window.config(padx=100, pady=100)
#window["padx"] = 50
#window["pady"] = 50 # Same thing, both changes the above window class attributes

label = Label(text="Label 1")

button1 = Button(text="Button 1")

button2 = Button(text="Button 2", padx=5, pady=5)

entry = Entry()

label.grid(column=1, row=1)
button1.grid(column=3, row=1)
button2.grid(column=2, row=2)
entry.grid(column=4, row=3)

window.mainloop()
