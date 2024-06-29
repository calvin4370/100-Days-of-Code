import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_COLOUR = "darkorchid"

class Snake:
    def __init__(self):
        # Initialise Turtles i.e. The Snake Segments to starting positions
        self.segments = []
        self.create_snake() # NOTE THAT SELF HAS TO BE PUT FIRST FOR CLASS METHODS TO BE USED ON ITSELF (THE OBJECT)

        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    # Add segment to the snake at a certain position, not to be confused with extend snake, which calls this function inside
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color(SNAKE_COLOUR)
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)

    # Moves the snake body i.e. segments[1:], following the fronter segment  
    def move(self):
        # Every following segment moves to the old position of the preceding segment
        for index in range(len(self.segments)-1, 0, -1): # Range is from index of last segment to index of 2nd segment
            # Get position of the next segment, firster
            fronter_segment_pos = self.segments[index-1].position()
            self.segments[index].goto(fronter_segment_pos)
            
        # Move segments[0] forward
        self.segments[0].forward(20)
        
    # Turns the snake head up, if its not already going down
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    # Turns the snake head down, if its not already going up
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    # Turns the snake head left, if its not already going right
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # Turns the snake head right, if its not already going left
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # Extend snake by addinga segment, for when the snake eats a food
    # NOTE: This is a higher order function meant to simplify finding position of last segment and adding a segment there
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    # Trigger an effect on the snake when game over
    def game_over(self):
        index = 0
        print("Arrrggghhhh! De Snake is DEAD!")
        for segment in self.segments:
            index += 1
            segment.color("firebrick")
            time.sleep(0.1)
        for segment in self.segments:
            segment.hideturtle()
            time.sleep(0.1)
        