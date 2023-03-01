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

# we want these to maintain state
#invariant variable = don't want in the loop
done = False
result = []
turns = 0

#  used so we can shuffle the life of colors each time we run through the game
order = list(hitboxes.keys())

# Mainloop
# each time through the while is one frame

while not done: #true
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(order)
                turns = len(order)
                result = []
                for color in order:
                    for c, hb in hitboxes.items():
                        pygame.draw.rect(screen,main_colors[c],hb)
                    pygame.draw.rect(screen,highlight_colors[color],hitboxes[color])
                    pygame.display.flip()
                    pygame.time.delay(1000)
            elif event.key == pygame.K_q:
                done = True
        elif event.type == pygame.MOUSEDOWNBUTTON:

# Idea of top down programming - outline program first and put in the details later
#  use the word pass 

    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         pass
    #     elif event.type == pygame.MOUSEDOWNBUTTON:
    #         pass
    #     elif event.type == pygame.KEYUP:
    #         pass










