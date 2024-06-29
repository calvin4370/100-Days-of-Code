import tkinter
"""
Default window size: 
The window will automatically scale to include all the buttons and stuff you put in it

Packer
------
Labels will be packed to fit the space by taking center by default, but not expanded to take all space
"""
# Initialise the Tkinter window
window = tkinter.Tk()
window.title("My 1st GUI Program")
window.minsize(width=500, height=500)


# Create a Label
label1 = tkinter.Label(text="Fuwawa", font=("Calibri", 24, "bold"))
label1.pack()

label2 = tkinter.Label(text="Mococo", font=("Calibri", 24, "bold"))
label2.pack()

label3 = tkinter.Label(text="Gura", font=("Calibri", 24, "bold"))
label3.pack(side="left")

label4 = tkinter.Label(text="Amelia", font=("Calibri", 24, "bold"))
label4.pack(side="right")

label3 = tkinter.Label(text="Nene", font=("Calibri", 24, "bold"))
label3.pack(side="bottom")

label3 = tkinter.Label(text="Suisei", font=("Calibri", 24, "bold"))
label3.pack(side="bottom")


# Main window loop to keep window onscreen
window.mainloop()