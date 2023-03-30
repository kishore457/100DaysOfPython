import turtle as turtle_module
import random
color_list = [(150, 40, 131), (47, 48, 145), (249, 237, 16), (250, 254, 252), (253, 243, 249), (179, 182, 30), (246, 240, 3), (125, 196, 101), (218, 41, 16), (234, 45, 31), (251, 252, 254), (147, 30, 83), (206, 133, 160), (44, 132, 119), (75, 159, 123), (241, 161, 176)]

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed(0)

# move to initial position

"""
setheading()
0 - east
90 - north
180 - west
270 - south
"""


tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # go to next line only when 10 dots are drawn
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


















screen = turtle_module.Screen()
screen.exitonclick()
