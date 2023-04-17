def starpyramid(star): #Behind the scenes: rows = levels 
    for s in range(1,star+1):
        symbol = "*"
        print(symbol*s)

def rstar_pyramid(star):
    for s in range(star,0,-1): #If we put levels in here instead, it would be a global variable 
        symbol = "*"
        print(symbol*s)

# range(start,stop,step)

# scope 
levels = int(input("Enter the desired pyramid height: "))

starpyramid(levels)
rstar_pyramid(levels)

#-------------------#
# 3/8 In Class Notes 

def foo(x,y,z):
    print(foo(x,y,z))

foo(1,2,3)
foo(2,1,3)
foo(3,2) # Error: Not enough parameters

# Python has 2 different ways of passing parameters
    # we can give these variables named paramters
def bar(x=0,y=2,z=3):
    print(x,y,z)

bar(z=1,x=2)
bar()

# Anything outside of a function is global scope
    # global_var = 5 #global scope
    # def luv():
    #     local_var = 5 
    #     x = 2 #local variables get deleted when function ends
    #     # Paramters are local variables

    # def luv():
    #     local_var = 5 
    #     print(x) #Will not work here because x is only a variable in the other function 

# Mathematical def of a function would be f(x) = y
#  Functions must return a value 

# def foo():
#     x = 5 
#     #return Nune: Nonetype

# def bar():
#     if x is None:
#         x = 5*2
#     #return Nune: Nonetype

# print(foo())

# We can return one thing 
# if we use commas, we can have it return multiple multiple values in one tuple 

def foo():
    x = 5 
    return x #Not returning x, just the value 5
    #return x, 4

y = foo()
print(y)

# Function ends once we use the return command

# def my_func(x=0):
#     return x+x #x is scoped here

# my_func(5)
# print(x) # Error here because x is only scoped within my_func

# def powerof(x=0,p=0):
#     power = p
#     y = x ** power
#     return y

# power = 2
# result = powerof(5,3)
# print(result)

def foo():
    x = 5
    print(x*x)
    # If you dont have a return, it will return none no matter what

def foo2():
    x = 5
    return x*x

print(foo()) #nested functions execute from the inside out
print(foo2())

# We follow certain conventions 

# def fooBar():
#     x = 5
#     y = 6
#     return x * y

# def foo_bar():
#     x = 5
#     y = 6
#     return x * y

# .pdf
# .py

# Problem
# 10000 line program, we could accidently assign the variable twice and cause conflict - AKA name collisions 
# Global variable never leaves memory while the program is running
# This can take up a lot of memory!
var = 5

def start():
    print(var)

def main(): #main functions
    x = 5
    start(x)


# We are going to start putting all code from global scope into this main function, which eliminates global scope

### ONLY THING IN GLOBAL SCOPE IS CALLING THE MAIN FUNCTION ###
# Always call at the end of your program 

main()

