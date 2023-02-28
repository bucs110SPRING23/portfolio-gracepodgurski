import pygame
import random
pygame.init()

while 1:
    pygame.event.pump()
    screen = pygame.display.set_mode()
    screen.fill ("white")
    dimensions = screen.get_size()
    print(dimensions)
    center = [dimensions[0]//2, dimensions[1]//2]
    dimensions = screen.get_size()
    print(dimensions)
    starting_point = [dimensions[0]//2, dimensions[1]//2]

    pygame.draw.circle(screen,"yellow",center, 525)

    # distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
    # is_in_circle = distance_from_center <= width/2 #screen width

    pygame.time.wait(5000)

    break 

# Still working on this... I have been sick so I  am still trying to catch up  with this lab and the previous one
