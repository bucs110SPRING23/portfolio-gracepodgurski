
sides = int(input("Please enter the number of sides:  "))
length = int(input("Please enter the length of the sides:  "))
angle = 360 / sides


import math
import turtle
pen = turtle.Turtle()
turtle.forward(length)
turtle.right(angle)
window = turtle.Screen()

window.exitonclick()

# This code needs more work, but not required in class on 2/8




