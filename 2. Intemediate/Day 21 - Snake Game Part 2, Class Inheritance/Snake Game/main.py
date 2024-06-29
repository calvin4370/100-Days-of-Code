import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE = {"width": 600, "height": 600}
INITIAL_SPEED = 0.1 # This is not turtle's speed, but is the time.sleep value between frames in sec

# Initialise Screen
screen = Screen()

screen.setup(width=SCREEN_SIZE["width"], height=SCREEN_SIZE["height"])
screen.bgcolor("midnightblue")
screen.title("Turtle Snake Game")
# Turn screen tracer off and animations off, you now have to update the screen every time you want a new frame
screen.tracer(0)


# Initialise the Snake and Food, snake 2nd to put it on top
food = Food()
snake = Snake()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        snake.extend_snake()
        food.respawn()
        scoreboard.increment_score()
        scoreboard.update_scoreboard()
    
    # Detect collision with wall
    if snake.head.xcor() > 290:
        snake.head.setx(-300)
    
    elif snake.head.xcor() < -290:
        snake.head.setx(300)

    elif snake.head.ycor() > 290:
        snake.head.sety(-300)

    elif snake.head.ycor() < -290:
        snake.head.sety(300)
    
    # Detect collision of head with 2nd segment and after of the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            screen.tracer(1)
            snake.game_over()
            food.game_over()
            scoreboard.game_over()
            break

# Screen Main Loop
screen.mainloop()