import pygame
import random
import math
pygame.init()


def even_odd(num):
    while True:
        for i in num:
            if i % 2 == 0:
                return True
            else:
                return False


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


    score = 0
    for i in range(20):
        while even_odd(True):
            friend = score
            x = "blue"
        while even_odd(False):
            myself = score
            x = "orange"

        x = random.randrange(0,1050)
        y = random.randrange(0,1050)
        dart = [x,y]
        distance_from_center = math.hypot(abs(525-x),abs(525-y)) #the distance formula

        if distance_from_center <= 525: #screen width
            pygame.draw.circle(screen,x,dart, 5)
            score = score + 1
        else:
            pygame.draw.circle(screen,"red",dart, 5)
        pygame.display.flip()
        pygame.time.wait(2000)

    print("My score is :", myself)
    print("Your score is: ", friend)

    break

    # font = pygame.font.Font(None, 48)
    # text = font.render(<your message>, True, "white")
    # screen.blit("text", (<x>, <y>)) # where <x> and<y> are coordinates on screen