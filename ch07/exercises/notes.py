# managing complexity - advanced programming just manages complexity 

# Unix = original version was 10,000 SLOC (source lines of code)
# Chrome = 10,000,000 SLOC
# Windows (OS X) = 100,000,000 SLOC

# Complex objects 
#  - primitives:  int,str,floar,lists,dict,tuple
#  - turtle: x(int),y,heading,color(str),pensize(int),shape(str)

# We could create a dictonary 
#  myturtle: {x(int),y,heading,color(str),pensize(int),shape(str)}

# Instead, we want to create a way to bundle data and functions together 
# - state: the current values of the data in the object
# - behavior: the functions that cna operate on the data in the object

# Point object/class 
# - object should do one thing
# state: x,y,color
# behavior:color_change, move

# classes = type

# classes are blueprints for objects
# - functions are stored algorithms 
# - class as a stored data type 
# - classes are not executable 
# - don't put executable code in global scope,  definitions are fine

# Point Class
#  - instance: an object created from a specific class
    # t = turtle.Turtle() #t is an instance of turtle
# - instance variable: an internal variable that is part of an instance
#   - t.x, t.pos #x and pos are instance variables
# - interface: the functions and variables of an object
    # t.forward() #.forward() part of the interface of turtle

# Point - make itt a class ourselves

# def make_point(x,y)
class Point:
    # classes always start with a capital letter
    # - usually, classes go in their own file
    # -1 class per file 
    # - dunders = double  underscores on both sides of the name
    def __init__(self):
        self.x = 0 #dot  operator accesses instance variables of object
        y = 0
        color = ""

### main.py
import point 

p1  = point.Point()
p1.x = 10

p2 = point.Point()
p2.x = 5

p1.color = "red"


