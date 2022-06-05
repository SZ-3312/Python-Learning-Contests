from turtle import Turtle
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = MOVE_DISTANCE
        self.cheat_counters = 0
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def up(self):
        self.forward(self.move_distance)

    def dash(self):
        self.forward(self.move_distance * 2)

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def cheat(self):
        self.goto(0, 280)
        self.cheat_counters += 1





