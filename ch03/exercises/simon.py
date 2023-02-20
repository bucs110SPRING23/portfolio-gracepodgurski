## Event (Graphical programming)
# Operating system handles events 
# Your program -> OS: anything happened?
# Events that could happen: 
    #click (click of the mouse)
    #key presses 
# OS => event
# types of event == operation 

#Trying to connect actions to algorithms 

# Example: Simon Says 
import pygame
pygame.init()

screen = pygame.display.set_mode()
colors = ["red","green","blue,"yellow"]
random.shuffle(colors)

for colors in colors:

