from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("classic")
timmy.color("green")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screener = Screen()
screener.exitonclick()


# importing from internet :0 
import heroes
print(heroes.gen())

