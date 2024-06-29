import random
from turtle import Turtle
"""
We want each Food object to be a Turtle from the turtle module
But we also want each food item to inherit the attributes and methods of the Turtle class
So we will employ class inheritance
"""

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("olivedrab3")
        self.speed("fastest")
        self.penup()

        self.respawn() # NOTE MAKE SURE TO CALL SELF WHEN YOU ARE CALLING A CLASS METHOD WITHIN THE CLASS

    def respawn(self):
        self.teleport(int(random.randint(-14, 14) * 20), int(random.randint(-14, 14) * 20))
    
    def game_over(self):
        self.hideturtle()