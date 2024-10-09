from turtle import Turtle, Screen
import turtle as t
import random


# RANDOM WALK

tim = Turtle()
tim.shape("arrow")
tim.color("PaleGreen4")

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]
turt_colors = ["light yellow", "aquamarine4", "dark slate blue", "gold1", "lawn green", "indianRed", "lavender",
               "firebrick", "turquoise4", "coral", "deep pink"]

tim.pensize(10)
tim.speed(10)
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.pencolor(random_color())
