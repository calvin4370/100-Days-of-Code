import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.color("DarkOliveGreen")
turtle.speed(10)
turtle.pensize(10)


# Change the appearance of the screen
screen.title("My Turtle")


# Command the turtle
turtle.pendown()

colors = ["firebrick", "tomato", "LightGoldenrod", "chartreuse2", "aquamarine", "DodgerBlue4", "DarkOrchid", "DarkViolet"]
turnings = [turtle.left, turtle.right]
angles = [0, 90, 180]

def execute(function, arg):
    function(arg)

def random_walk():
    turtle.pencolor(random.choice(colors))
    turtle.forward(30)

    execute(random.choice(turnings), random.choice(angles))

turtle.dot(20, "black")

for i in range(200):
    random_walk()

turtle.penup()
turtle.setheading(0)
turtle.forward(250)
turtle.right(90)


# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()
