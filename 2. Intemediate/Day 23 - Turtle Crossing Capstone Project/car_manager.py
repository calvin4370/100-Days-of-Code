import random
import math
from turtle import Turtle

COLORS = ["firebrick", "tomato", "goldenrod", "chartreuse3", "dodgerblue", "darkorchid"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SPAWN_CARS_ON_THIS_TICK = 45
CARS_TO_SPAWN_AT_START = 45
CARS_TO_SPAWN_PER_CYCLE = 16

level = 1
player_position = [0, -280]

class CarManager:
    def __init__(self):
        self.fleet = []
        self.level = 1
        self.tick = 0

        self.spawn_car("start")

    def spawn_car(self, mode="start"):
        if mode == "start":
            for i in range(CARS_TO_SPAWN_AT_START):
                car = Car(spawn_xcor=random.randint(-270, 440))
                self.fleet.append(car)

        elif mode == "continue":
            if self.tick == SPAWN_CARS_ON_THIS_TICK:
                for i in range(CARS_TO_SPAWN_PER_CYCLE):
                    car = Car(spawn_xcor=random.randint(310, 600))
                    self.fleet.append(car)
                print(f"car_manager: {CARS_TO_SPAWN_PER_CYCLE} cars spawned from right")
                self.tick = 0
            else:
                self.tick += 1

    def move_cars(self):
        for car in self.fleet:
            car.move()
    
    def level_up(self):
        self.level += 1
        global level
        level += 1
        print(f"car_manager level is now {self.level}")
    
    def despawn_offscreen_cars(self):
        for car in self.fleet:
            if car.xcor() <= -320:
                car.hideturtle()
                self.fleet.remove(car)
    
    def despawn_all_cars(self):
        for car in self.fleet:
            car.hideturtle()
        self.fleet = []
    
    def game_over(self):
        for car in self.fleet:
            car.crash()
        self.despawn_all_cars()

    def up(self):
        global player_position
        player_position[1] = player_position[1] + 10

class Car(Turtle):
    def __init__(self, spawn_xcor=320):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.speed(10)
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1.5)
        self.goto((spawn_xcor, random.randint(-240, 240)))
        self.setheading(180)
    
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE +  MOVE_INCREMENT * (level - 1))
    
    def calc_bearing_to_player(self):
        # Let A be the car position, and B be the player turtle position
        A = self
        B = player_position

        opp = B[1] - A.ycor()
        adj = B[0] - A.xcor()

        bearing = math.atan(opp/(adj+0.001)) # + 0.001 to account for 0
        return bearing
    
    def calc_dist_to_player(self):
        # Let A be the car position, and B be the player turtle position
        A = self
        B = player_position

        AB_2 = (A.xcor()-B[0])**2 + (A.ycor()-B[1])**2
        AB = math.sqrt(AB_2)
        return AB
    
    def crash(self):
        self.setheading(self.calc_bearing_to_player())
        self.forward(self.calc_dist_to_player())
        self.hideturtle()


