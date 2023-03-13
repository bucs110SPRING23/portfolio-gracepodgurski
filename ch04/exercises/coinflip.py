import turtle
import random

window = turtle.Screen()

player1 = turtle.Turtle()
player1.color("green")
player1.shape("turtle")
player1.speed(0)

distance = 10
angle = 90
in_screen = True 

while in_screen:
    coin = random.randrange(0,2)
    if coin:
        player1.right(angle)
    else:
        player1.left(angle)
    player1.forward(distance)

    turtleX = player1.xcor()
    turtleY = player1.ycor()

    x_range = window.window_width()  / 2
    y_range = window.window_height() / 2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        in_screen = False

# Instead  of doing it this way, we can turn this into a function



