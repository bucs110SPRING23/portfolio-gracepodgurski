import turtle
import random

def center():
    pistil = turtle.Turtle()
    pistil.color("yellow")  
    pistil.up()  
    pistil.goto(0,-66)
    center_rad = 85
    pistil.down()
    pistil.fillcolor('yellow')
    pistil.begin_fill()
    pistil.circle(center_rad)
    pistil.end_fill()
    
def stem():
    stalk = turtle.Turtle()
    stalk.color("green")
    stalk.pensize(15)
    stalk.up()
    stalk.goto(35,-80)

    stalk.right(70)
    stalk.down()
    stalk.forward(300)


# ----- Main Code ------
def main():
    petal_color = str(input("What color would you like your flower to be? "))
                      
    window = turtle.Screen()
    window.bgcolor("black")

    pencil = turtle.Turtle()
    pencil.color(petal_color)    

    pencil.up()
    pencil.goto(-250,-25)
    pencil.fillcolor(petal_color)
    pencil.begin_fill()
    
    pencil.down()

    for s in range(9):
        pencil.forward(500)
        pencil.left(160)

    pencil.end_fill()

    center()
    stem()

    window.exitonclick()

main()

#  Used this website for tips for drawing the petals https://www.tutorialspoint.com/turtle-programming-in-python

# def create_turtle():
#     # try to create a code to create turtles for you
#     return 