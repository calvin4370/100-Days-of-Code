import pandas
import random
from tkinter import *

WORD_BANK_CSV = "data/french_words.csv"

BACKGROUND_COLOR = "#B1DDC6"
SHADOW = "#392467"
ORCHID = "#5D3587"
EGGPLANT = "#A367B1"
PEACH = "#FFD1E3"

LANGUAGE_FONT = ("Arial", 36, "italic")
WORD_FONT = ("Arial", 64, "bold")
BUTTON_FONT = ("Arial", 22, "bold")

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)


# ------------------------------ Handling csv data ------------------------------ #
dataframe = pandas.read_csv(WORD_BANK_CSV)
list_of_word_dicts = dataframe.to_dict(orient="records")
""" --> [{'French':'French word', 'English':'English word'}, ...] """

remaining_word_list = list_of_word_dicts
""" --> [{'French':'French word', 'English':'English word'}, ...] """


# ------------------------------ Button Functions ------------------------------ #
def correct():
    global current_word_pair
    
    if remaining_word_list:
        remaining_word_list.remove(current_word_pair)
        next_card()
    else:
        deck_finished()

def wrong():
    global current_word_pair

    remaining_word_list.append(current_word_pair)
    next_card()

def next_card():
    """Grab a french-english pair item: {'French':'French word', 'English':'English word'} \n
    from the list_of_word_dicts derived from the dataframe made from the word bank csv \n
    and switch the flashcard displayed to the corresponding one"""
    global current_word_pair
    current_word_pair = random.choice(remaining_word_list)

    # Ensure card is facing up
    flashcard_canvas.itemconfig(card_face, image=flashcard_front_img)

    flashcard_canvas.itemconfig(language, text="French", fill=SHADOW)
    flashcard_canvas.itemconfig(word, text=current_word_pair["French"], fill=SHADOW)

def flip():
    """Flips the current flashcard from French to English or English to French"""
    global current_word_pair
    if flashcard_canvas.itemcget(language, "text") == "French":
        flashcard_canvas.itemconfig(card_face, image=flashcard_back_img)
        flashcard_canvas.itemconfig(language, text="English", fill=SHADOW)
        flashcard_canvas.itemconfig(word, text=current_word_pair["English"], fill=SHADOW)
    else:
        flashcard_canvas.itemconfig(card_face, image=flashcard_front_img)
        flashcard_canvas.itemconfig(language, text="French", fill=SHADOW)
        flashcard_canvas.itemconfig(word, text=current_word_pair["French"], fill=SHADOW)

def deck_finished():
    flashcard_canvas.itemconfig(card_face, image=flashcard_front_img)

    flashcard_canvas.itemconfig(language, text="Study Complete", fill=SHADOW)
    flashcard_canvas.itemconfig(word, text=f"You finished {len(list_of_word_dicts)} flash cards!", fill=SHADOW)

# ------------------------------ Row 1: Flashcard Canvas (3ex1) ------------------------------ #
flashcard_front_img = PhotoImage(file="images/card_front.png")
flashcard_back_img = PhotoImage(file="images/card_back.png")

flashcard_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_face = flashcard_canvas.create_image(400, 263, image=flashcard_front_img)
flashcard_canvas.grid(column=1, row=1, columnspan=3)

language = flashcard_canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT, fill=SHADOW) # Remember these texts don't need to be assigned to a variable
word = flashcard_canvas.create_text(400, 300, text="word", font=WORD_FONT, fill=SHADOW) # But if you do, you can access and change the text as you wish


# ------------------------------ Row 2: Correct, Wrong and Flip Buttons ------------------------------ #
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong)

flip_button = Button(text="Flip", font=BUTTON_FONT, fg=SHADOW, bg=PEACH, padx=40, pady=10, highlightthickness=0, command=flip)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=correct)

wrong_button.grid(column=1, row=2)
flip_button.grid(column=2, row=2)
correct_button.grid(column=3, row=2)


# Get 1st card
next_card()

window.mainloop()