# More notes - kind of a part 2 to the other notes file
# In a GUI, everything will be in classes

## Controller - like  a model, label for how a class is used

# Model - data
# View - display (pygame)
# Controller - logic (director)

"""
file: main.py
"""
# different classes (in  different files in the same folder) contain the different parts of the code that we will import here
# Controller class, graph class
from src.controller import Controller

def main():
    controller = Controller()
    controller.mainloop()


main()

#  A sprite is an object which moves around and interacts on the screen 
#   not required in pygame 

# You can inherit something and add something to it rather than retyping the code

def update(self):
    self.rect =+ 1

#  Use this to make something move every frame 

#  Sprite groups - self.points = pygame.Group