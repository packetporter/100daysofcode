# from turtle import Turtle, Screen
#
# johnte = Turtle()
# johnte.shape("turtle")
# johnte.color("DarkOrchid1")
# johnte.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table.align)
print(table)