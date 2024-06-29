import random
import time
from turtle import Turtle, Screen

from snake import Snake

INITIAL_SPEED = 0.1 # This is not turtle's speed, but is the time.sleep value between frames in sec

# Initialise Screen
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("midnightblue")
screen.title("Turtle Snake Game - Part 1")
# Turn screen tracer off and animations off, you now have to update the screen every time you want a new frame
screen.tracer(0)


# Initialise the Snake
snake = Snake()


# Start Event Listening
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Main Game Loop
game_on = True
while game_on:
    # Update screen only after all segments move so as to not get choppy segment by segment movement with gaps between segments
    screen.update()
    time.sleep(INITIAL_SPEED)

    snake.move()


# Screen Main Loop
screen.mainloop()