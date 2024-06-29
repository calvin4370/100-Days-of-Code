import tkinter
"""
Labels will be packed to fit the space by taking center by default, but not expanded to take all space
"""
# Initialise the Tkinter window
window = tkinter.Tk()
window.title("My 2nd GUI Program")
window.minsize(width=500, height=500)


# Create a Label
label1 = tkinter.Label(text="Fuwawa", font=("Calibri", 24, "bold"))
label1.pack()

# Change Label parameters
label1["text"] = "Mococo"
label1.config(text="Mococo") # Same thing

# Create a Button
def nuclear_launch():
    print(f"{label1["text"]} launched a nuclear missile!")
    button2["text"] = "Click Me Again!"

def switch():
    if label1["text"] == "Fuwawa":
        label1["text"] = "Mococo"
    elif label1["text"] == "Mococo":
        label1["text"] = "Fuwawa"

button1 = tkinter.Button(text="Switch", font=("Calibri", 24, "bold"), command=switch)
button1.pack()

button2 = tkinter.Button(text="Click Me", font=("Calibri", 24, "bold"), command=nuclear_launch)
button2.pack()



# Main window loop to keep window onscreen
window.mainloop()