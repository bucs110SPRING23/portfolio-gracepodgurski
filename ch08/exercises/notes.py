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

    # double under (dunder)
    # no paramters  other 'self'
    # must return a string
    def __str__(self) -> str:
        
        pass 
    
# object functions are called methods 
# using self  as the first parameter makes it a method
# methods only work on one type of data as opposed to a function which can take many types




    def addone(self) -> None:
        self.data += 1
        #  by using self.var, i change the scope of the data to  an object, not a method (or function)

class Foo:
    def __init__(self,**kwargs) -> None:
        self.__dict__ = kwargs


    # def __init__(self,x,y,z,a,b,c) -> None:
    #     pass

def main():
    mynum = Num(7)
    mynum2 = Num(9)
    mynum3 = {'data':7,'x':'string'}


    print(mynum.data)
    print(mynum2.data)
    print(mynum3['data'])
    print(mynum3.__dict__)

    mynum.addone() #objects from a class are called instances of the class
    print(mynum.data)
    mynum2.addone()
    print(mynum2.data)

    dictionary = {'x':1,'y':2,'z':3}
    foo = Foo(**dictionary) # x = 1, y = 2, z = 3

    t = turtle.Turtle()
    t.forward(56)

    mylist = [] #list(), str()
    mylist.forward() #Error
    mylist.append()
    index = 0
    mylist.pop(index) #removes

    num = 5
    # print("My number is:" + str(num))
    print(f"The number is: {num}")
    mynewnum = Num(5)
    print(f"The number is: {mynewnum}")



main()
