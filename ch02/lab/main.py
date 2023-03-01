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


#Part B - Drawing Shapes 

pygame.init()
window = pygame.display.set_mode()

side_length = 200
dimensions = window.get_size()
xpos = dimensions[0]//2
ypos = dimensions[1]//2


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
    # pygame.Surface.fill(window,"black",)
    # pygame.display.flip()





