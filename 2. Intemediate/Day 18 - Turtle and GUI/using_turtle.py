from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.color("DarkOliveGreen")
turtle.speed(2.5)


# Change the appearance of the screen
screen.title("My Turtle")


# Command the turtle
turtle.pendown()

def dotted_line(distance):
    for i in range(int(distance/10)):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)

for i in range(4):
    dotted_line(100)
    turtle.right(90)

turtle.penup()
turtle.forward(250)
turtle.right(90)


# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()
