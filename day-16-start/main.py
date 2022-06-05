#
# from turtle import Turtle, Screen
#
# tom = Turtle()
# my_screen = Screen()
# tom.shape("turtle")
# tom.color("purple")
# tom.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Greninja", "Talonflame"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)