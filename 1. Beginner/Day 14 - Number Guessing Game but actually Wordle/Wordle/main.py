import random
import terminal_colourer as tc

# Global Variables (though lists won'r bring up problems anyways):
# player_guesses = ["_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _"] # A list of up to 6 5-letter strings, which are the player's guesses
green_letters = [] # A list of letters the player has picked which turned green
yellow_letters = [] # A list of letters the player has picked which turned yellow
red_letters = [] # A list of letters the player has picked which turned red 
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

global guess_number
guess_number = 0

def main():
    print("Welcome to Wordle!")

    # Main Game Loop
    while True:
        # Reset global variables on start of a new Wordle game
        global guess_number, player_guesses, green_letters, yellow_letters, red_letters
        guess_number = 0
        player_guesses = ["_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _"]
        green_letters, yellow_letters, red_letters = [], [], []
        
        global wordle_answer
        wordle_answer = get_answer().rstrip()
        global solved
        solved = False

        # Each iteration of this loop is a guess for the player to make
        for i in range(6): 
            print_box()
            player_guess = get_guess()
            edit_box(player_guess)
            # print(f"However, global solved: {solved}") # Testing
            if solved:
                print_box()
                break
        
        # If solved before 6th guess
        if solved:
            congrats_lines = [f"You solved the Wordle with your 1st guess! Did you cheat?",
                              f"You solved the Wordle in only {guess_number} guesses! Well done",
                              f"You solved the Wordle in just {guess_number} guesses! Amazing!",
                              f"You solved the Wordle in {guess_number} guesses! Splendid work.",
                              f"You solved the Wordle in {guess_number} guesses! Not bad."]
            print(congrats_lines[guess_number])
            prompt_continue()
            continue

        # Last chance: 6th guess
        if solved:
            print("You solved the Wordle with your last guess! Good save!")
        else:
            print_box()
            print(f"You didn't get the answer, the correct word is {wordle_answer}.")
        
        prompt_continue()
        continue

# Prints the main interface for players to see their 6 guesses and a keyboard,
# Box includes the Wordle game title, the 6 guesses coloured, the coloured keyboard alphabet list and prompt for player guess
def print_box():
    print("\n\n  W o r d l e  ")
    print("---------------")
    # print(f"Answer is {wordle_answer} btw ~") # For testing
    index = 0
    for i in range(6):
        print(f"({index+1}) {player_guesses[index]}")
        index += 1
    spawn_alphabet()

def get_guess():
    global guess_number
    guess_number += 1
    player_guess = input(f"Guess {guess_number}: ").upper()
    while True:
        if len(player_guess.strip()) != 5 or player_guess.isalpha() == False:
            player_guess = input(f"Input a 5 letter word! Guess {guess_number}: ").upper()
            continue
        elif valid_guess(player_guess) == False:
            player_guess = input(f"'{player_guess}' is not in our word list! Guess {guess_number}: ").upper()
            continue
        else:
            break
    
    return player_guess

# Edits the player_guesses list so that print_box() with print an updated list of the player's guesses, Colours are updated here
def edit_box(latest_guess):
    new_string = ""
    index_of_letter = 0
    correct_letters = 0
    for letter in latest_guess:
        if letter == wordle_answer[index_of_letter]: # letter in guess matches correct letter exactly, letter turns green
            slotted_letter = tc.green(letter)
            green_letters.append(letter)
            correct_letters += 1
        elif letter in wordle_answer:
            slotted_letter = tc.yellow(letter) # letter in guess appears in answer but not at that position, letter turns yellow
            yellow_letters.append(letter)
        else:
            slotted_letter = tc.red(letter) # letter in guess does not appear in answer, letter turns red
            red_letters.append(letter)
        new_string += slotted_letter + " "
        index_of_letter += 1
    
    new_string = new_string.rstrip()
    player_guesses[guess_number-1] = new_string
    if correct_letters == 5:
        global solved
        solved = True

# Spawns the alphabet of untried letters in white, correct letters in green and yellow, and wrong letters in red
def spawn_alphabet():
    alphabet_line = ""
    for letter in alphabet:
        if letter in green_letters:
            alphabet_line += tc.green(letter) + " "
        elif letter in yellow_letters:
            alphabet_line += tc.yellow(letter) + " "
        elif letter in red_letters:
            alphabet_line += tc.red(letter) + " "
        else:
            alphabet_line += letter + " "
    print(alphabet_line.rstrip())

# Picks a 5-letter word from the list of 2,315 possible Wordle answers as the answer
def get_answer():
    with open("answers.txt", "r") as file:
        global possible_wordlist
        possible_wordlist = file.readlines()
        answer = random.choice(possible_wordlist).upper()

    return answer

def valid_guess(latest_guess):
    validity = False
    with open("other_valid_guesses.txt", "r") as file:
        other_valid_guesses_list = file.readlines()
        valid_guesslist = possible_wordlist + other_valid_guesses_list
        for word in valid_guesslist:
            if word.strip().upper() == latest_guess:
                validity = True
                break

    return validity


def prompt_continue():
    response = input("Do you want to play again (y/n)? ")
    while True:
        if response[0].lower() == "y":
            break
        elif response[0].lower() == "n":
            print("Game ended. Thanks for playing!\n")
            quit()
        else:
            response = input("Do you want to play again (y/n)? ")
            continue

if __name__ == "__main__":
    main()