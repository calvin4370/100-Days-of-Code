import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_SIZE = {"width": 800, "height": 600}

# Initialise the Screen
screen = Screen()
screen.setup(width=SCREEN_SIZE["width"], height=SCREEN_SIZE["height"])
screen.bgcolor("springgreen4")
screen.title("Turtle Pong")
# Turn screen tracer off and animations off, you now have to update the screen every time you want a new frame
screen.tracer(0)


# Initialise the Paddles, Ball and Scoreboard
paddle1, paddle2 = Paddle(1), Paddle(2)
ball = Ball()
scoreboard  = Scoreboard()


# Start Event Listening
screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")

screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

screen.onkeypress(ball.clear, "space")

screen.onkey(quit, "p")


# Main Game Loop
game_on = True
while game_on:
    screen.update()
    ball.move()

    # Detect collision of ball with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    
    # Detect collision of ball with paddles
    # We can't simply use ball.distance(paddle) < 20 since the turtle.distance() method measures distance between the centres of each turtle object
    if -340 > ball.xcor() > -360 and abs(paddle1.ycor() - ball.ycor()) < 55:
        ball.paddle_bounce()

    if 330 < ball.xcor() < 350 and abs(paddle2.ycor() - ball.ycor()) < 55:
        ball.paddle_bounce()

    # Detect ball evading paddles
    if ball.xcor() > 440:
        scoreboard.increment_player1()
        ball.reset()
        screen.update()
        time.sleep(1)
        ball.start(2)
    elif ball.xcor() < -440:
        scoreboard.increment_player2()
        ball.reset()
        screen.update()
        time.sleep(1)
        ball.start(1)

    time.sleep(0.005)


screen.mainloop()