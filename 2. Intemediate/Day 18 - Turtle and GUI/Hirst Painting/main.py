"""
Antipyralazo III by Turtle Hirst
50 x 41 dots
Draw dots from x=-245 to x=245 (50 dots wide) and from y=-200 to y=200 (41 dots wide)
"""
import random
from colour_palette import bg_colour, spot_colours
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle
turtle.shape("turtle")
turtle.shapesize(2.00, 2.60)
turtle.color("DarkOliveGreen")
turtle.speed(0)


# Change the appearance of the screen
screen.title("Damien Hurst the Turtle Paints a Million Pound Painting")
screen.colormode(255) # Set color rgb from 0 to 255 instead of default 0 to 1.0
screen.bgcolor(bg_colour)


# Command the turtle
def hirst():
    print("Turtle Hirst is beginning to paint a million pound artwork.")
    turtle.penup()
    turtle.goto(-490, 400)
    y_level = 400

    for h in range(41):
        print(f"Turtle Hirst: Painting Line {h+1}/41")
        for w in range(50):
            turtle.dot(10, random.choice(spot_colours))
            turtle.forward(20)

        y_level -= 20
        turtle.goto(-490, y_level)
    
    turtle.goto(550, -400)
    turtle.right(90)
    print("Turtle Hirst: Doya!? I call this piece 'Antipyrylazo Turtle'")

hirst()


# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()
