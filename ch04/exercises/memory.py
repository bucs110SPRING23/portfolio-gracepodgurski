import random
import pygame

pygame.init()
screen = pygame.display.set_mode()

(width,height) = pygame.display.get_window_size() #(w,h)
#  returns as a tuple of 2 items (w,h)
#  this is a trick but functions can not return more than one value 

#  Create hitboxes
hit_box_width = width/2
hit_box_height = height/2

# 2 halves make quarter
#  rectangle objects - keep track of size and position on  screen

# sets up the box objects, does not position them
hitboxes = {
    "red": pygame.Rect(0,0,hit_box_width,hit_box_height),
    "green": pygame.Rect(0,0,hit_box_width,hit_box_height),
    "blue": pygame.Rect(0,0,hit_box_width,hit_box_height),
    "purple": pygame.Rect(0,0,hit_box_width,hit_box_height),
    }

#  position hitboxes
hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purrple"].topleft = hitboxes["red"].bottomright

# define  hitbox colors
main_colors = {
    "red": (200,0,0),
    "green": (0,200,0),
    "blue": (0,0,200),
    "purple": (200,0,200),
}

#define hitbox colors
highlight_colors = {
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "purple": (255,0,255),   
}

#additional state  data
font = pygame.font.Font(None,48)
done = False
result = []
turns = 0
order = list(hitboxes.keys())

# Mainloop
# each time through the while is one frame

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            





