import pygame
import math
pygame.init()

while 1:
    pygame.event.pump()

    window = pygame.display.set_mode()

    side_length = 10
    xpos = 100
    ypos = 50

    points = []
    sides = 3
    rest = [4,6,20,100,360]

    for s in range(sides):
        angle = 360/sides
        radians = math.radians(angle * s)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])

    pygame.draw.polygon(window, "pink", points)
    # pygame.display.flip()
    pygame.time.wait(5000)
    break
