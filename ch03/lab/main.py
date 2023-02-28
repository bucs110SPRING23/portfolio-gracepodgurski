import pygame
import random
pygame.init()

screen = pygame.display.set_mode()

while 1:
    pygame.event.pump()

    dimensions = screen.get_size()
    print(dimensions)
    starting_point = [dimensions[0]//2, dimensions[1]//2]



    pygame.time.wait(2000)
    break 

