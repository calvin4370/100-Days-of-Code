from turtle import Turtle
"""
We want the Scoreboard object to be a Turtle from the turtle module
But we also it inherit the attributes and methods of the Turtle class
So we will employ class inheritance
"""

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("cornsilk")
        self.goto(0, 270)

        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "bold"))
    
    def increment_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
    
    def game_over(self):
        self.clear()
        self.goto(0, 20)
        self.write("GAME OVER", False, "center", ("Arial", 40, "bold"))
        self.goto(0, -20)
        self.write(f"You scored {self.score} points", False, "center", ("Arial", 24, "bold"))