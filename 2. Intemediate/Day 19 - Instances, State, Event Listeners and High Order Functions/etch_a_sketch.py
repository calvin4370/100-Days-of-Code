from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.color("DarkOliveGreen")
turtle.pensize(8)
turtle.speed(5)


# Change the appearance of the screen
screen.title("My Turtle")


# Write functions
# This is to be passed to the other functions as we cant call the turtle method directly in some of the functions
def move_forwards():
    turtle.forward(15)

def move_backwards():
    turtle.backward(15)

def turn_left():
    turtle.left(20)

def turn_right():
    turtle.right(20)

def clear_and_reset():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

# Add Event Listening
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_and_reset, "space")

# Command the turtle
turtle.pendown()




# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()