import turtle as t
import random


t.colormode(255)

tim = t.Turtle()
tim.pensize(10)
tim.speed("fastest")


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "wheat", "LightSeaGreen"]

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # tuple_list = []
    # tuple_list.append(r)
    # tuple_list.append(g)
    # tuple_list.append(b)
    # rgb_tuple = tuple(tuple_list)
    # print(rgb_tuple)
    # return rgb_tuple

    random_color = (r, g, b)
    return random_color

for _ in range(200):
#     tim.color(random.choice(colours))
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)



