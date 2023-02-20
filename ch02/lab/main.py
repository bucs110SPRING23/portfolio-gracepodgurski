#Part A

import turtle 
import random

window = turtle.Screen()

# #Race 1
# don = turtle.Turtle()
# don.color("black")
# don.shape("turtle")
# don.up()

# mic = turtle.Turtle()
# mic.color("red")
# mic.shape("turtle")
# mic.up()

# don.goto(-100,20)
# mic.goto(-100,-20)
# don.down()
# mic.down()
# don.forward(random.randrange(1,100))
# mic.forward(random.randrange(1,100))

# window.exitonclick()

#Race 2
raph = turtle.Turtle()
raph.color("blue")
raph.shape("turtle")
raph.up()
raph.goto(-100,20)

leo = turtle.Turtle()
leo.color("green")
leo.shape("turtle")
leo.up()
leo.goto(-100,-20)

for s in range(0,10):
    raph.down()
    raph.forward(int(random.randrange(1,10)))
    leo.down()
    leo.forward(int(random.randrange(1,10)))

window.time.wait(20000)
window.exitonclick()

#Part B - Drawing Shapes 
# triangle
# square
# hexagon (6 sides)
# icosagon (20 sides)
# Hectagon (100 sides)
# circle -ish (360 sides)

import pygame 
import math
pygame.init()
window1 = pygame.display.set_mode()

points = [10,10]
side_length = int(50)
num_sides = int()

pygame.draw.polygon(window1, "pink", points)
