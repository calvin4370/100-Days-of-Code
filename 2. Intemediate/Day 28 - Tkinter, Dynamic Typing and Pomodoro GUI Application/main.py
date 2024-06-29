from tkinter import *
"""
NOTE: Learning Point
--------------------
- You cannot have while loops in your program while a mainloop is going on as they will clash
- Thus, you will have to make use of tkinter's functionalities for timer setups
"""
# ---------------------------- CONSTANTS ------------------------------- #
"""
COLOURS from colorhunt.co
"""
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2 #25
SHORT_BREAK_MIN = 0.2 #5
LONG_BREAK_MIN = 0.2 #20
rep=0
# Making a global variable timer, initialising it to None, so 1 function can assign it and another function can access and change it
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    global rep
    window.after_cancel(timer)
    timer = None

    title_label.config(text="Timer", fg=GREEN,font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_text, text="00:00", fill="seashell")
    ticks.config(text="", fg=GREEN)
    rep = 0
    start_button.config(text="Start")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    global timer
    rep += 1

    if rep in [1, 3, 5, 7]: # These are the work reps
        title_label.config(text="Work", fg=RED)
        if timer:
            window.after_cancel(timer) # Cancel the previous after instance so no problems arise if start is pressed during a work or rest cycle
        countdown(WORK_MIN * 60)
    if rep in [2, 4, 6]: # These are the short breaks
        title_label.config(text="Short Break", fg=GREEN)
        tick_count = ticks["text"]
        ticks["text"] = tick_count + " ✔"
        if timer:
            window.after_cancel(timer)
        countdown(SHORT_BREAK_MIN * 60)
    elif rep == 8: # This is the long break
        ticks["text"] = "✔ ✔ ✔ ✔"
        title_label.config(text="Long Break", fg=PINK)
        if timer:
            window.after_cancel(timer)
        countdown(LONG_BREAK_MIN * 60)
    elif rep >= 9:
        title_label.config(text="End of Pomodoro Cycle!", fg=GREEN, font=(FONT_NAME, 25, "bold"))
        timer = None
        canvas.itemconfig(timer_text, text="00:00", fill="seashell")
    # NOTE: In a situation where we might have 100s of reps or something, use % to get it by factor of 2, 8 etc.
    
    start_button.config(text="Skip")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    global timer

    canvas.itemconfig(timer_text, text=f"{int(minutes):02d}:{int(seconds):02d}")
    if seconds > 0:
        timer = window.after(1000, countdown, seconds - 1) # You don't have to assign this to a variable, but we're doing it here to access timer it in reset()
    elif seconds == 0:
        timer = window.after(1000, start_timer)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.minsize(570, 500)
window.config(padx=100, pady=50, bg=YELLOW)



# Use Tkinter's Canvas widget (class) to canvas images
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0) # Size of the widget in pixels
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image) # Many of these types of methods can be overlapped onto the same canvas, the dimensions start from 0, 0 at the top left hand corner
                                                  # you want the image put smack in the middle of the canvas so use half, abit ot the right so its not cut off by the borders
timer_text = canvas.create_text(102, 132, text="00:00", font=(FONT_NAME, 35, "bold"), fill="seashell") # You can do this without assigning it to a variable, but in this case, we want to
canvas.grid(column=2, row=2)



# Put the rest of the widgets
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=2, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), bg=GREEN, command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 16, "bold"), bg=GREEN, command=reset, highlightthickness=0)
reset_button.grid(column=3, row=3)

ticks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
ticks.grid(column=2, row=3)





window.mainloop()