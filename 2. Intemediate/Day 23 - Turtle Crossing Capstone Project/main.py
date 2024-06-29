import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
def on_up():
    player.up()
    car_manager.up()

screen.onkeypress(on_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Spawn cars every certain number of frames
    car_manager.spawn_car("continue")

    # Advance cars leftwards
    car_manager.move_cars()

    # Despawn cars that go off the left screen
    car_manager.despawn_offscreen_cars()

    # Detect when turtle reaches finish line
    if player.ycor() >= FINISH_LINE_Y:
        player.go_to_start_pos()
        car_manager.level_up()
        scoreboard.level_up()
    
    # Detect collision of car with player turtle
    for car in car_manager.fleet:
        if car.distance(player) < 30:
            game_is_on = False
            player.game_over()
            screen.tracer(1)

car_manager.game_over()
scoreboard.game_over()

screen.mainloop()