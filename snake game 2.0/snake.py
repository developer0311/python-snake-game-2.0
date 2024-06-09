from turtle import Turtle
import time


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.segments[0].forward(20)

    def add_segment(self, position):
        self.new_segment = Turtle("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        

    def move_fast(self):
        self.segments[0].forward(5)
        self.move()
