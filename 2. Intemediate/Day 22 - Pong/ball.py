import random
from turtle import Turtle

BALL_SPEED = 2 # This does not refer to turtle.speed(), rather it refers to number of pixels ball moves per frame / time.sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color("seashell")
        self.penup()
        self.goto(-5, 0)

        self.start(0)
    
    def start(self, player=0):
        self.paddles_can_hit = True # Prevents bounce spam bug
        self.walls_can_bounce = True
        if player == 0:
            self.setheading(random.choice([random.randint(30, 60), random.randint(120, 150), random.randint(210, 240), random.randint(300, 330)]))
            self.forward(BALL_SPEED)
        elif player == 1:
            self.setheading(random.choice([random.randint(130, 150), random.randint(220, 240)]))
            self.forward(BALL_SPEED)
        elif player == 2:
            self.setheading(random.choice([random.randint(30, 50), random.randint(310, 330)]))
            self.forward(BALL_SPEED)

    def move(self):
        self.positive_heading()
        self.forward(BALL_SPEED)
        self.vary_trajectory()

        if -5 < self.xcor() < 5:
            self.paddles_can_hit = True
            self.walls_can_bounce = True
        
        if -5 < self.ycor() < 5:
            self.walls_can_bounce = True
            

    def wall_bounce(self):
        self.positive_heading()
        if self.walls_can_bounce:
            self.setheading(360 - self.heading())
            self.vary_trajectory(5, 10)
            self.dot(5, "blue")
            self.walls_can_bounce = False
            self.forward(BALL_SPEED)

        # if 0 <= self.heading() < 90:
        #     self.setheading(360 - self.heading())
        # elif 90 <= self.heading() < 180:
        #     self.setheading(360 - self.heading())
        # elif 180 <= self.heading() < 270:
        #     self.setheading(360 - self.heading())
        # elif 270 <= self.heading() < 3600:
        #     self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.positive_heading()

        if 270 <= self.heading() < 360 or 0 <= self.heading() < 90 and self.paddles_can_hit: # Going to P2
            self.setheading(self.heading() * -1 + 180)
            self.paddles_can_hit = False
            self.walls_can_bounce = True
            self.dot(10, "skyblue")
            self.vary_trajectory(10, 30)

            self.forward(BALL_SPEED)

        elif 180 <= self.heading() < 270 or 90 <= self.heading() < 180 and self.paddles_can_hit: # Going to P1
            self.setheading(self.heading() * -1 + 180)
            self.paddles_can_hit = False
            self.walls_can_bounce = True
            self.dot(10, "orchid2")
            self.vary_trajectory(10, 30)

            self.forward(BALL_SPEED)
        
        elif self.paddles_can_hit == False:
            print("ERROR: pandle_bounce() called when paddles_can_hit == False")
        
    def positive_heading(self):
        if self.heading() >= 360:
            self.heading(self.heading() // 360)
        elif self.heading() <= -360:
            self.setheading(self.heading() // 360)
        
        if self.heading() < 0:
            self.setheading(360 - self.heading())
    
    def reset(self):
        self.goto(-5, 0)
    
    def vary_trajectory(self, min=0, max=0):
        self.setheading(self.heading() + random.choice([random.randint(min, max), random.randint(min, max) * -1]))