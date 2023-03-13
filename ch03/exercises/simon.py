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
import random
pygame.init()

screen = pygame.display.set_mode()
colors = ["red","green","blue","yellow"]
random.shuffle(colors)

for colors in colors:
    screen.fill(colors)
    pygame.display.flip()
    pygame.time.wait(2000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(2000)

message = """
    Simon Says:
    UP:RED
    DOWN: BLUE
    LEFT: GREEN
    RIGHT: YELLOW
    
    click on the window, enter a sequence, then press enter
"""

response = input(message)

#pygame.EVENT_OBJECT
user_sequence = []
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            screen.fill("red")
            user_sequence.append("red")
        elif event.key== pygame.K_DOWN:
            screen.fill("blue")
            user_sequence.append("blue")
        elif event.key== pygame.K_LEFT:
            screen.fill("green")
            user_sequence.append("green")
        elif event.key== pygame.K_RIGHT:
            screen.fill("yellow")
            user_sequence.append("yellow")
    print("user_sequence = ",user_sequence)
    print("colors = ",colors)
    ## Need to finish this 