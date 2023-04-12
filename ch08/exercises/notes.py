### Notes 
# 
# Today: Start milestone 1 for midterm

## Methods
#  last time, we looked at classes - which give us the ability to connect the data and the algorithm
#  - a class is almost like  a library & allows us to organize our code
#  class == type 
#  use 'class' for user-defined types
# "complex type"

#  

import turtle

class Num:

    def __init__(self, n) -> None:
        self.data = n #instance variables for Num type objects


def main() -> None:
    mynum = Num(7)
    mynum2 = Num(9)

    print(mynum.data)
    print(mynum2.data)

    t = turtle.Turtle()
    t.forward(56)


main()
