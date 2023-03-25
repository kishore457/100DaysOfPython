from turtle import Turtle
from turtle import Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")
timmy_the_turtle.color("deeppink")
# moves 1000 phases
timmy_the_turtle.forward(100)

# turns 90 degrees
timmy_the_turtle.right(100)
timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()