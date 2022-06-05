import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard_crossing import Scoreboard
from tkinter import messagebox


def main_func():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    messagebox.showinfo("How To Play", "w/e/up arrow to move forward\n"
                                       "Try to cross the street without being hit by the cars!")
    screen.tracer(0)
    p = Player()
    car = CarManager()
    sb = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)

        sb.update()
        screen.listen()
        screen.onkey(p.up, "Up")
        screen.onkey(p.cheat, "Down")
        screen.onkey(p.dash, "e")
        screen.onkey(car.level_up, "l")

        car.make_car()
        car.make_truck()
        car.move_vehicles()

        if p.ycor() >= 280:
            p.reset_pos()
            car.level_up()
            sb.increase_level()

        for c in car.cars:
            if c.distance(p) <= 20:
                sb.game_over()
                game_is_on = False

        for t in car.trucks:
            if t.distance(p) <= 35:
                sb.game_over()
                game_is_on = False

        screen.update()

        if p.cheat_counters >= 3:
            sb.game_over()
            game_is_on = False

        elif sb.level >= 50:
            sb.win_game()
            game_is_on = False

    screen.exitonclick()
