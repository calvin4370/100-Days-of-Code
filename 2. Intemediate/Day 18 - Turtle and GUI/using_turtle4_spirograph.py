from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.color("DarkOliveGreen")
turtle.speed(0)


# Change the appearance of the screen
screen.title("Using Turtle to Draw a Spirograph")


# Command the turtle
turtle.pendown()

for i in range(1, 73):
    turtle.circle(200)
    turtle.right(5)

turtle.penup()
turtle.forward(500)
turtle.right(90)


# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()
