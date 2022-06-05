from turtle import Turtle
from random import randint, choice
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.max_num = 6
        self.rounds = 0
        self.cars = []
        self.trucks = []
        self.make_car()

    def make_car(self):
        chance = randint(1, self.max_num)
        if chance == self.max_num:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.turtlesize(stretch_len=2, stretch_wid=0.5)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-260, 280))
            self.cars.append(new_car)

    def make_truck(self):
        chance = randint(1, self.max_num * 5)
        if chance == self.max_num * 5:
            new_truck = Turtle()
            new_truck.penup()
            new_truck.shape("square")
            new_truck.turtlesize(stretch_len=3, stretch_wid=1)
            new_truck.color(choice(COLORS))
            new_truck.goto(300, randint(-240, 260))
            self.trucks.append(new_truck)

    def move_vehicles(self):
        for turtle in self.cars:
            turtle.backward(self.move_distance)

        for turtle in self.trucks:
            turtle.backward(self.move_distance - 1)

    def level_up(self):
        self.rounds += 1
        if self.move_distance < 45:
            self.move_distance += MOVE_INCREMENT
        if self.max_num > 1 and self.rounds % 2 == 0:
            self.max_num -= 1
