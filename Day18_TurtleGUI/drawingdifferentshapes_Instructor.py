import random
import turtle as t

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "wheat", "LightSeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    rand_color = random.choice(colours)
    tim.color(rand_color)
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)