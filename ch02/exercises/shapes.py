import pygame
pygame.init()

screen = pygame.display.set_mode()


pygame.draw.circle(screen, "pink", [200,150], 50)
pygame.display.flip()
pygame.time.wait(2000)

