#Part A

import turtle 
import random
# don = random.randrange(1,100)
# mic = random.randrange(1,100)

window = turtle.Screen()

# #Race 1
# pen1 = turtle.Turtle()
# pen1.color("black")
# pen1.goto(-100,20)
# pen1.forward(don)

# pen2 = turtle.Turtle()
# pen2.color("red")
# pen2.goto(-100,-20)
# pen2.forward(mic)


# window.exitonclick()


#Race 2
# raph = int(random.randint(1,10))
# leo = int(random.randint(1,10))
# myturtles = [raph,leo]
# print(myturtles)

# for s in range(myturtles):
# pen1 = turtle.Turtle()
# pen1.color("black")
# pen1.goto(-100,20)
# pen1.forward(don)

# pen2 = turtle.Turtle()
# pen2.color("red")
# pen2.goto(-100,-20)
# pen2.forward(mic)

# window.exitonclick()

#Race 2.1
def createTurtlePlayer(color, startx, starty): 
    player=turtle.Turtle()
    player.color(color) # set the color of turtle
    player.shape("turtle") #set the shape as turtle
    player.penup() #pen moves up
    player.goto(startx, starty) #place player at mentioned position on race

raph =createTurtlePlayer('red',-100,20)
leo =createTurtlePlayer("blue",-100,-20)
myturtles = (raph,leo)

for s in range(myturtles):
    raph.forward(int(random.randrange(1,10)))
    leo.forward(int(random.randrange(1,10)))
    window.time.wait(20000)
window.exitonclick()