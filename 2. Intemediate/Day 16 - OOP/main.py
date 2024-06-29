from turtle import Turtle, Screen
from prettytable import PrettyTable

# turtle = Turtle()
# screen = Screen()
table = PrettyTable()

# turtle.shape("turtle")
# turtle.color("darkolivegreen")
# turtle.forward(100)

table.field_names = ["Pokemon", "Type(s)"]
table.add_rows(
    [
        ["Charmander", "Fire"],
        ["Squirtle", "Water"],
        ["Bulbasaur", "Grass"],
        ["Pikachu", "Electric"]
    ]
)
table.align = "l"
print(table)

# screen.exitonclick()