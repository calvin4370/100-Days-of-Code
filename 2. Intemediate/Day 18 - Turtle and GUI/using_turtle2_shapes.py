from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.color("DarkOliveGreen")
turtle.speed(4)
turtle.pensize(5)


# Change the appearance of the screen
screen.title("My Turtle")


# Command the turtle
turtle.teleport(-200, 200)
turtle.pendown()

colors = ["firebrick", "tomato", "LightGoldenrod", "chartreuse2", "aquamarine", "DodgerBlue4", "DarkOrchid", "DarkViolet"]
color_number = 0

for sided_shape in range(3,11):
    turtle.pencolor(colors[color_number])
    for side in range(sided_shape):
        turtle.forward(150)
        turtle.right(360/sided_shape)

    color_number += 1

turtle.penup()
turtle.forward(250)
turtle.right(90)


# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()
