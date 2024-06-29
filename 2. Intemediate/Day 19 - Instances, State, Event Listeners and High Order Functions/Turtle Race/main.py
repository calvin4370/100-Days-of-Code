import random
from turtle import Screen
from race_functions import screen, init_turtles, race


# Command the turtles
init_turtles()
race()

# Run Screen mainloop, screen will not disappear immediately upon program running 
screen.mainloop()