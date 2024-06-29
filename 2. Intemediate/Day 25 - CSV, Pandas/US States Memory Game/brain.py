import pandas
import turtle

class Brain(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.unguessed_states = []
        self.get_unguessed_states()
        self.guessed_states = []

        self.penup()
        self.hideturtle()
        self.goto(-400, 300)

    def get_unguessed_states(self):
        unguessed_states = []
        with open("50_states.csv", "r") as file:
            self.data = pandas.read_csv(file)
            states_data = self.data["state"]
            for state in states_data:
                self.unguessed_states.append(state)
    
    def write_state(self, state):
        x = self.data[self.data.state == state.title()]["x"]
        y = self.data[self.data.state == state.title()]["y"]

        self.goto((int(x.iloc[0]), int(y.iloc[0])))
        self.write(state.title(), True, "center", ("Calibri", 12, "bold"))


brain = Brain()
brain.get_unguessed_states()