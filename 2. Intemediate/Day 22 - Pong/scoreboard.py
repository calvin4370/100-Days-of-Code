from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("seashell")
        self.hideturtle()
        self.penup()
        self.goto(-5, 240)

        self.score1 = 0
        self.score2 = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score1} : {self.score2}", False, "center", ("Courier", 36, "bold"))
    
    def increment_player1(self):
        self.score1 += 1
        self.clear()
        self.update_scoreboard()
    
    def increment_player2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()
