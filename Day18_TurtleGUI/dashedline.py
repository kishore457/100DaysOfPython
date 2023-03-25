from turtle import Turtle
from turtle import Screen


tim = Turtle()
tim.shape("classic")

for _ in range (15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()