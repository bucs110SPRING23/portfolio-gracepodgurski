#Part A

import turtle 
import random
don = random.randrange(1,100)
mic = random.randrange(1,100)

window = turtle.Screen()

pen1 = turtle.Turtle()
pen1.color("black")
pen1.goto(-100, 20)

pen2 = turtle.Turtle()
pen2.color("red")
pen2.goto(-100,-20)



window.exitonclick()
