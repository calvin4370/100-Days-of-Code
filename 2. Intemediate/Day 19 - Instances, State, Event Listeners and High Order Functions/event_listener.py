from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.color("DarkOliveGreen")
turtle.speed(2.5)


# Change the appearance of the screen
screen.title("My Turtle")


# Write functions
# This is to be passed to the other functions as we cant call the turtle method directly in some of the functions
def move_forwards():
    turtle.forward(10)


# Add Event Listening
screen.listen()
screen.onkey(move_forwards, "Up")


# Command the turtle
turtle.pendown()




# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()