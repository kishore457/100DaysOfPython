import another_module
print(another_module.another_variable)

import turtle

timmy = turtle.Turtle() #initialize or contruct object from blueprint


from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)

# attributes
my_screen = Screen()
print(my_screen.canvheight)


# methods
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(90)
my_screen.exitonclick()



