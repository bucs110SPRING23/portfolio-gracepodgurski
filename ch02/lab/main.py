#Part A

import turtle 
import random
import pygame
import math

window = turtle.Screen()

#Race 1
don = turtle.Turtle()
don.color("black")
don.shape("turtle")
don.up()

mic = turtle.Turtle()
mic.color("red")
mic.shape("turtle")
mic.up()

don.goto(-100,20)
mic.goto(-100,-20)
don.down()
mic.down()
don.forward(random.randrange(1,100))
mic.forward(random.randrange(1,100))

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

raph.up()
raph.goto(-100,20)
leo.up()
leo.goto(-100,-20)

# window.time.wait(20000)
# window.exitonclick()

#Part B - Drawing Shapes 
#As of 2/20, I'm still trying to figure out this part

pygame.init()
window = pygame.display.set_mode()
# Sides:
# tri = 3
# squ = 4
# hex = 6
# ico = 20
# hect = 100
# cir = 360

side_length = 50
xpos = 200
ypos = 200


# Create a for loop outside of the triangle one and make it applicable for all shapes
points = []
sides=[3,4,6,20,100,360]

for i in sides:
    for s in range(i):
        angle = 360/i
        radians = math.radians(angle * s)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])

    pygame.draw.polygon(window, "pink", points)
    pygame.display.flip()
    pygame.time.wait(2000)
    # sides_spot = int(sides[i+1])

