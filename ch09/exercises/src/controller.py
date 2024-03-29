import pygame
import random
import  pygame_menu

from src.ball import ball

class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()

        self.width = size[0]
        self.height = size[1]

        self.colors = {"purple": [150, 25, 150]}

        ## Bouncing Ball Model
        self.ball = Ball(self.width / 2, self.height / 2, 50)
        self.sprites = pygame.sprite.Group((self.ball,))

        self.state = "GAME"


    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endloop()
            elif self.start == "START":
                self.startloop()

    def startloop(self):
        self.menu = pygame_menu.Menu("Start Screen",self.width/2,self.height/2)
        self.menu.add.label("Click to start program",font_size = 28)
        self.menu.add.button("Start",self.startgame ,align=pygame_menu.locals.ALIGN_CENTER)

        while self.state == "START":
            self.menu.update(pygame.get.events())
            self.menu.draw()
            self.menu.draw(self.screen)
            pygame.display.flip()



    def endloop(self):
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("You won",)

        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.blit(msg, (50,50))
            pygame.display.flip()


        

    def gameloop(self):

        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        self.state  == "END"
        
        while True:

            # update the ball's position
            self.ball.move()

            # adjust the direction of the ball based on position
            if self.ball.y < 0:
                self.ball.direction = "down"
            elif self.ball.y > self.height:
                self.ball.direction = "up"

            ## Check the limit, if outside of screen, change direction

            self.screen.fill(self.colors["purple"])

            pygame.draw.circle(
                self.screen,
                self.ball.get_color(),
                (self.ball.x, self.ball.y),
                self.ball.size,
            )
            pygame.display.flip()

def startgame(self):
    self.state = "GAME"