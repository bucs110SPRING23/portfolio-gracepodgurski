import pygame
pygame.init()

screen = pygame.display.set_mode()


pygame.draw.circle(screen, "white", [200,150], 50)
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.circle(screen, "white", [200,250], 78)
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.circle(screen, "white", [200,350], 100)
pygame.display.flip()
pygame.time.wait(2000)