# import colorgram
#
# colors = colorgram.extract("rainbow.jpeg", 20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as t
import random
t.colormode(255)

tim = t.Turtle()
screen = t.Screen()
color_list = [(150, 40, 131), (47, 48, 145), (249, 237, 16), (250, 254, 252), (253, 243, 249), (179, 182, 30), (246, 240, 3), (125, 196, 101), (218, 41, 16), (234, 45, 31), (251, 252, 254), (147, 30, 83), (206, 133, 160), (44, 132, 119), (75, 159, 123), (241, 161, 176)]
tim.shape("classic")


def draw_dot():
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.forward(10)
def draw_dot_line(number_of_dots):

    for _ in range(number_of_dots):
        draw_dot()
        tim.color("white")
        tim.forward(40)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.backward(50*number_of_dots)

for _ in range(10):
    draw_dot_line(10)




screen.exitonclick()