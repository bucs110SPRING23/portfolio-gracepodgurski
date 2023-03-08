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

    myself = 0
    friend = 0
    # players = [myself,friend]

    for i in range(1,11):
        x = random.randrange(0,1050)
        y = random.randrange(0,1050)
        dart = [x,y]
        distance_from_center = math.hypot(abs(525-x),abs(525-y)) #the distance formula
        if (i % 2) == 0:
            x = "blue"
            if distance_from_center <= 525: #screen width
                pygame.draw.circle(screen,x,dart, 5)
                friend = friend + 1
            else:
                pygame.draw.circle(screen,"red",dart, 5)
            pygame.display.flip()
            pygame.time.wait(2000)
        else:
            x = "yellow"
            if distance_from_center <= 525: #screen width
                pygame.draw.circle(screen,x,dart, 5)
                myself = myself + 1
            else:
                pygame.draw.circle(screen,"red",dart, 5)
            pygame.display.flip()
            pygame.time.wait(2000)
    if myself > friend:
        print("I won! The score is:", myself,":", friend)
        message = "I won! The score is:", myself,":", friend
    elif friend > myself:
        print("You won! The score is: ", friend,":", myself)
        message = "You won! The score is: ", friend,":", myself
    else:
        print("I guess we are good opponents... it's a tie", myself,":" ,friend)
        message = "I guess we are good opponents... it's a tie", myself,":" ,friend
    break

#  Still trying to figure out the part below
font = pygame.font.Font(None, 48)
text = font.render(message, True, "white")
screen.blit(text, (200, 200)) # where <x> and<y> are coordinates on screen