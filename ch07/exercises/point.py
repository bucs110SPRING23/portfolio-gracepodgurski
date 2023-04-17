# this all should be in a main.py code instead
import random
import point
import pygame
from pygame import Rect

def  mainloop(display):
    points = []
    while True:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pooint_deleted = False
                for p in points:
                    if p.Rect.collidepoint(event.pos):
                        print(event.pos,p.rect.center)
                        del p
                        point_deleted = True
                    if not point_deleted:
                        # p = point.Point(*event.pos)
                        p = point.Point(event.pos[0],event.pos[1])
                        points.append(p)
            # fill in more of this code with reference to the professor's
        pygame.draw.circle(display,p.color,p.rect.pos,p.rect.h/2)
        
        display.fill("white")
        pygame.display.flip()

def main():
    pygame.init()
    display = pygame.display.set_mode()
    mainloop(display)