import random
import turtle as t

# create turtle object

tim = t.Turtle()
tim.shape("classic")
tim.speed(10)
tim.pensize(10)
random_direction = ["forward", "backward", "right", "left"]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "wheat", "LightSeaGreen"]
def random_walk():
    direction = random.choice(random_direction)
    if direction == "forward":
        tim.forward(25)
    elif direction == "backward":
        tim.backward(25)
    elif direction == "right":
        tim.right(90)
        tim.forward(25)
    else:
        tim.left(90)
        tim.forward(25)


for _ in range(100):
    random_walk()
    tim.color(random.choice(colours))
