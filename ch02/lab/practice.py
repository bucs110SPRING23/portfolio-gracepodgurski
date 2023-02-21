import pygame
import math
pygame.init()

window1 = pygame.display.set_mode()
# Sides:
# tri = 3
# squ = 4
# hex = 6
# ico = 20
# hect = 100
# cir = 360

side_length = 200
xpos = 200
ypos = 200


# Create a for loop outside of the triangle one and make it applicable for all shapes
points = []
sides=3
rest = [4,6,20,100,360]

for s in range(sides):
    angle = 360/sides
    radians = math.radians(angle * s)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window1, "pink", points)
pygame.time.wait(2000)
#pygame.display.flip()
    # sides_spot = int(sides[i+1])
    # sides_spot = int(sides[i+1])

