from turtle import Turtle
FONT = ("Courier", 24, "bold")
SCORE_POSITION = (-200, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.update()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def win_game(self):
        self.update()
        self.goto(0, 0)
        self.color("gold")
        self.write("YOU WIN THE GAME!", align="center", font=FONT)
