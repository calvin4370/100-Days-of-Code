from turtle import Turtle

UI_POSITION = (-210, 260)
FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 48, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("darkslategrey")
        self.penup()
        self.goto(UI_POSITION)
        

        self.level = 1
        self.update_level_shown()
    
    def update_level_shown(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.level += 1
        self.update_level_shown()

        print(f"Level Up! Current level: {self.level}")

    def game_over(self):
        self.clear()

        self.goto(0, 30)
        self.write("GAME OVER", False, "center", GAME_OVER_FONT)
        self.goto(0, -10)
        self.write(f"You reached Level {self.level}", False, "center", FONT)
