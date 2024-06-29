import random
from turtle import Turtle, Screen

# Initialise Screen
screen = Screen()
screen.title("Turtle Race 1")

# Initialise the race location and turtles
nicky, ricky, dicky, dawn, start_helper, end_helper = Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()
racer_names = ["Nicky", "Ricky", "Dicky", "Dawn"]
turtles = [nicky, ricky, dicky, dawn, start_helper, end_helper]
colours = ["darkgoldenrod", "cadetblue", "firebrick", "hotpink", "black", "black"]

# Get user input
turtle_chosen = ""
while turtle_chosen.title() not in racer_names:
    turtle_chosen = screen.textinput("Which turtle do you think will win the race?", "                    Nicky/Ricky/Dicky/Dawn                    ")

# Variables
speeds = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
dists = [2, 3, 4, 7, 8, 10, 12, 12, 15, 18, 20, 25, 50]
x_start, y_start = -440, 60
x_end = 400
starting_line = (-400, 100)
finishing_line = (400, 100)

# Change appearance of the turtle cursor (by default some sort of arrow) to an actual turtle, set their locations up
def init_turtles():
    global y_start
    i = 0
    for turtle, colour in zip(turtles, colours):
        turtle.shape("turtle")
        turtle.color(colour)
        turtle.hideturtle()
        
        if turtle in turtles[0:4]:
            turtle.name = racer_names[i]
            i += 1

            turtle.penup()
            turtle.speed(1)
            turtle.teleport(x_start - 50, y_start)
            turtle.showturtle()
            turtle.finished = False
            y_start -= 40

            turtle.write(turtle.name, font=("Arial", 14, "bold"))

            turtle.forward(60)
        
        elif turtle == start_helper:
            turtle.speed(1)
            turtle.teleport(starting_line[0], starting_line[1])
            turtle.setheading(-90)
            turtle.showturtle()
        
        elif turtle == end_helper:
            turtle.speed(1)
            turtle.teleport(finishing_line[0], finishing_line[1])
            turtle.setheading(-90)
            turtle.showturtle()
    
    for helper in [start_helper, end_helper]:
        helper.pensize(10)
        helper.pencolor("grey")

    for i in range(18):
        start_helper.forward(10)
        end_helper.forward(10)

    for helper in [start_helper, end_helper]:
        helper.penup()
        helper.forward(30)
        helper.right(180)
    
    
def race():
    race_stop = False
    placings_list = ["1st", "2nd", "3rd", "4th"]
    placings_dict = {"Nicky":"", "Ricky":"", "Dicky":"", "Dawn":""}
    podium_dist = 60

    start_helper.left(90)
    start_helper.forward(25)
    start_helper.write("Start", font=("Arial", 16, "bold"))
    start_helper.forward(20)

    while race_stop == False:
        for turtle in turtles[0:4]:
            if not turtle.finished:
                turtle.speed(random.choice(speeds))
                turtle.forward(random.choice(dists))
            
            if turtle.xcor() > x_end + 20 and turtle.finished == False:
                placings_dict[turtle.name] = placings_list.pop(0)
                print(f"{turtle.name} came {placings_dict[turtle.name]}!")
                turtle.finished = True
                turtle.setx(x_end + podium_dist)
                turtle.write(f"    {placings_dict[turtle.name]}", font=("Arial", 14, "bold"))
                podium_dist -= 15
            
            # If all Turtles finished, stop the race loop
            if nicky.finished and ricky.finished and dicky.finished and dawn.finished:
                race_stop = True
            
    
    if placings_dict[turtle_chosen.title()] == "1st":
        end_helper.left(90)
        end_helper.write(f"You win! {turtle_chosen.title()} won the race!", move=True, font=("Arial", 16, "bold"))
        print(f"You win! {turtle_chosen.title()} won the race!")
    
    else:
        print(f"You lost! {turtle_chosen.title()} came {placings_dict[turtle_chosen.title()]}")
    