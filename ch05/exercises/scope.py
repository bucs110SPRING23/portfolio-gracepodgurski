
def multiply(num1,num2):
    mult = 0
    for _ in range(num2):
        mult = mult + num1
    return mult

def exponent(x1,x2):
    exp = 1
    for _ in range(x2):
        exp = exp * x1
    return exp 

def square(x):
    return exponent(x,2)


#  ---- MAIN CODE ------
def main():
    print(multiply(10,3)) 
    print(exponent(3,3))
    print(square(5))

main()