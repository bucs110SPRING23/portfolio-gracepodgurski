import turtle
sides = int(input("Please enter the number of sides:  "))
length = int(input("Please enter the length of the sides:  "))
angle = 360 / sides

pen = turtle.Turtle()
pen.color("black")


window = turtle.Screen()


for s in range(sides):
    pen.forward(length)
    pen.right(angle)
  

window.exitonclick()

# This code needs more work, but not required in class on 2/8




