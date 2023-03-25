from turtle import Turtle
from turtle import Screen

tim = Turtle()
screen = Screen()

tim.shape("classic")
tim.color("black")


angle = 360
drawn_ten_shapes = True
sides = 4
while drawn_ten_shapes:
    angle /= sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)
    if 10 == sides:
        drawn_ten_shapes = False
    sides += 1
    angle = 360
screen.exitonclick()
