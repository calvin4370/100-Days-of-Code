from turtle import Turtle
"""
Each Paddle consists of 1 solid square turtle object stretched to measure 100x20px
My old design wass for each paddle to be made up of 5 20x20 square segments lol
"""
# Constants and Variables
PADDLE_COLOUR_1 = "orchid2"
PADDLE_COLOUR_2 = "skyblue"
INITIAL_POSITIONS = [(-360, 0), (350, 0)]

class Paddle(Turtle):
    def __init__(self, player_num): #Recall that this is how you allow class calls to take argument inputs
        super().__init__()
        self.player_num = player_num
        self.initial_positions = [(-360, 0), (350, 0)]

        if int(player_num) == 1:
            self.shape("square")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.speed(0)
            self.color(PADDLE_COLOUR_1)
            self.penup()
            self.goto(INITIAL_POSITIONS[0])
        
        elif int(player_num) == 2:
            self.shape("square")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.speed(0)
            self.color(PADDLE_COLOUR_2)
            self.penup()
            self.goto(INITIAL_POSITIONS[1])
    
    def up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 25)
    
    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 25)
