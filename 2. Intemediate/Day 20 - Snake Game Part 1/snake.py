from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_COLOUR = "olivedrab3"

class Snake:
    def __init__(self):
        # Initialise Turtles i.e. The Snake Segments to starting positions
        self.segments = []
        self.create_snake() # NOTE THAT SELF HAS TO BE PUT FIRST FOR CLASS METHODS TO BE USED ON ITSELF (THE OBJECT)

        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.color(SNAKE_COLOUR)
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(position)

            self.segments.append(new_segment)
            print(position)

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