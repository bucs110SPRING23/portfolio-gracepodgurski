
import pygame
import random
import math
pygame.init()

while 1:
    # Part A: Setup
    pygame.event.pump()
    screen = pygame.display.set_mode((1050,1050))
    screen.fill("white")
    dimensions = screen.get_size()

    center = [dimensions[0]//2, dimensions[1]//2]

    pygame.draw.circle(screen,"black",center, 525)
    pygame.draw.circle(screen,"green",center, 524)
    pygame.draw.line(screen,"black",(dimensions[0]//2,0),(dimensions[0]//2,dimensions[1]))
    pygame.draw.line(screen,"black",(0,dimensions[1]//2),(dimensions[0],dimensions[1]//2,))
    
    pygame.display.flip()
    
    # Part B: Throwing darts
    
    # x = random.randrange(0,dimensions[0])
    # y = random.randrange(0,dimensions[1])
    # dart = [x,y]
    # pygame.draw.circle(screen,"black",dart, 5)

    # pygame.display.flip()
    # pygame.time.wait(2000)
    
    # print(x,y)

    for s in range(10):
        x = random.randrange(0,1050)
        y = random.randrange(0,1050)
        dart = [x,y]
        distance_from_center = math.hypot(abs(525-x),abs(525-y)) #the distance formula

        if distance_from_center <= 525: #screen width
            pygame.draw.circle(screen,"black",dart, 5)
        else:
            pygame.draw.circle(screen,"red",dart, 5)
        pygame.display.flip()
        pygame.time.wait(2000)

    break

# Still working on this... I have been sick so I  am still trying to catch up  with this lab and the previous one
