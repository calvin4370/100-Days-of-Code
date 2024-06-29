import tkinter
"""
Labels will be packed to fit the space by taking center by default, but not expanded to take all space
"""
# Initialise the Tkinter window
window = tkinter.Tk()
window.title("My 3rd GUI Program")
window.minsize(width=500, height=500)


# Functions
def set_winner():
    label2["text"] = entry1.get()

def reset():
    label2["text"] = "..."


# Create a Label
label1 = tkinter.Label(text="YouTuber of the Year", font=("Times New Roman", 24, "bold"))
label1.pack()
label2 = tkinter.Label(text="...", font=("Calibri", 18, "bold"))
label2.pack()

# Create an Entry
entry1 = tkinter.Entry(width=16, font=("Calibri", 16, "bold"))
entry1.pack()

button1 = tkinter.Button(text="Confirm", width=8, font=("Calibri", 16, "bold"), command=set_winner)
button1.pack()

button2 = tkinter.Button(text="Reset", width=6, font=("Calibri", 10, "bold"), command=reset)
button2.pack()

# Main window loop to keep window onscreen
window.mainloop()