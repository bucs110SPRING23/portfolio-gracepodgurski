import turtle
import random

def my_turtle():
    window = turtle.Screen()
    window.bgcolor("black")
    pencil = turtle.Turtle()
    pencil.color("pink")    

    pencil.up()
    pencil.goto(-250,-25)
    pencil.fillcolor('pink')
    pencil.begin_fill()
    
    pencil.down()
    for s in range(9):
        pencil.forward(500)
        pencil.left(160)

        # do this in a way where it can move around the middle of the circle
    pencil.end_fill()

    pencil.up()
    pencil.goto(0,-25)
    pistil = 50
    pencil.down()
    pencil.fillcolor('yellow')
    pencil.begin_fill()
    pencil.circle(pistil)
    pencil.end_fill()
    

    # pencil.up()
    # pencil.goto(150,0)
    # pencil.down()
    # pencil.circle(100)

    # pencil.up()
    # pencil.goto(-10,-100)
    # lips = 50
    # pencil.(lips)
    # pencil.down()

    # pencil.circle(100)
    
    window.exitonclick()

def main():
    my_turtle()

    # Insert code here... make it fun. 
main()