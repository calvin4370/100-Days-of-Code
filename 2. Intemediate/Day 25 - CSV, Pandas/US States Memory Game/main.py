import turtle
from brain import Brain
us_states_bg = "blank_states_img.gif"


# Setup the Screen
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(us_states_bg)
turtle.shape(us_states_bg)
screen.setup(width=800, height=600)


# Set up the Game Brain
brain = Brain()


# Main Game Loop
player_input = screen.textinput("US States Memory Game", "Enter a state")

game_on = True
while game_on:
    if player_input.title() in brain.unguessed_states:
        guessed_state = player_input.title()
        brain.unguessed_states.remove(guessed_state)
        brain.guessed_states.append(guessed_state)
        brain.write_state(guessed_state)
        player_input = screen.textinput("US States Memory Game", f"Correct! States: {len(brain.guessed_states)}/50")

    elif player_input.title() in brain.guessed_states:
        player_input = screen.textinput("US States Memory Game", f"You already guessed {player_input.title}, silly! States: {len(brain.guessed_states)}/50")
    
    elif player_input.lower() == "quit":
        print(f"Game ended. {len(brain.guessed_states)}/50 states guessed.")
    
    else:
        player_input = screen.textinput("US States Memory Game", f"{player_input.title} is not a US State, silly! States: {len(brain.guessed_states)}/50")
    
    # Detect if player has guessed all 50 states
    if len(brain.guessed_states) == 50:
        print("You win!")


# Screen Main Loop
screen.mainloop()