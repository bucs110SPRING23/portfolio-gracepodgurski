# def foo(param1, param2):
#     return param1 + param2
# # foo(1) would be an error - needs both parameters


# def bar(param1=4,param2=3): #default values aka named parameters 
#     local_var = 5 #scope is limited to the function
#     return param1 + param2 # Return ends the function 

# Default parameters not helpful when the two values need to be compared etc

# Don't use a blank list (any empty container) in the default values of a function 

def percentage_to_letter(percent=99):
    """
    This is a function that returns a letter grade based on a percentage 
    args: percent(int)
    return: letter(str)
    """
    # ^^ Above explains how a user will utilize the function; always put at the beginning 
    let = "A"
    if 80 <= percent < 90:
        let = "B"
    elif 70 <= percent < 80:
        let = "C"
    elif 60 <=percent < 70:
        let = "D"
    elif percent < 60:
        let = "F"
    return let
    
def is_passing(letter): #boolean function, is_... = convention for boolean 
    """
    This is a boolean function based on letters from percentage_to_letter function 
    args: letter(str)
    return: True or False
    """
    return letter in "ABCD" #"in" always gives boolean response 

# ----Main code below ----

def main(): #driver code
    # main does not require a doc string
    grades = [90, 85, 74, 62, 50]
    for grades in grades:
        letter = percentage_to_letter(grades)
        if is_passing(letter):
            print("You passed!")
        else:
            print("Better luck next time")

main()

# Programming Pattern

## for - programming pattern 

## accumulator pattern 
# result = 0 

# for i in range(10):
#     result = result + i

# print(result)

# accumulator = start_value 
# for i in list:
#     accumulator = accumulator <op> i

# def remove_vowels(string):
#     vowels = "aeiou"
#     vowels += vowels.upper()
#     result = ""
#     for ch in string:
#         if ch not in vowels:
#             result += ch 
#         return result 
    
# def main():
#     mystring = "Hello World"
#     mystring = remove_vowels(mystring)
#     print(mystring)

# main()