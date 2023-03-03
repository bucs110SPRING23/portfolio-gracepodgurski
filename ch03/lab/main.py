
import pygame
import random
pygame.init()

while 1:
    pygame.event.pump()
    screen = pygame.display.set_mode((1050,1050))
    screen.fill("white")
    dimensions = screen.get_size()

    center = [dimensions[0]//2, dimensions[1]//2]
    starting_point = [dimensions[0]//2, dimensions[1]//2]

    pygame.draw.circle(screen,"black",center, 525)
    pygame.draw.circle(screen,"orange",center, 524)
    pygame.draw.line(screen,"black",(dimensions[0]//2,0),(dimensions[0]//2,dimensions[1]))
    pygame.draw.line(screen,"black",(0,dimensions[1]//2),(dimensions[0],dimensions[1]//2,))
    
    pygame.display.flip()


    # distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
    # is_in_circle = distance_from_center <= width/2 #screen width

    pygame.time.wait(5000)
    break

# Still working on this... I have been sick so I  am still trying to catch up  with this lab and the previous one
