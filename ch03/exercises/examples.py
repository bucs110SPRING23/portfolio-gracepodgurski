# #In Class Examples
# #bool - boolean value 
#     #True/False
#     # *** -caps are important 
#     #True, 1, "Hello"

# print(type(True))
# print(bool(1), bool(-1), bool("hello"))

# #boolean expression

# x  = 5
# y = 10

# print(x == y) #equality
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# #or - if one is correct
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# # not - negation

# print(not True) #False

# #Example2
a = int(input("num:"))
if a < 0: #COLON
    a = abs(a)
else: #no condition, always optional
    print("positive")

print(a) #de-indentation to end the if statement

#if statements - only one condition will execute 
## All mutually exclusive statements, so we want most specific statement first
a = int(input("num:"))
if a > 10: #COLON
    print("x is greater than 10")
elif a > 5:
        print("x is greater than 5")

else: #no condition, always optional
    print("x is less than or equal to 5")

#elif 
#always goes between if and else, is optional, and can have as many as you'd like

## If <boolean condition>: #required
#   #do  something
## elif <boolean condition>: #optional
#   #do something
## else:     #optional 
#   #do something

### Fizzbuzz
# - loop through range of values supplied by the user
# - for each valuein the range
# - if the value is divisible by 3, print "fizz"
# - if the value is divisible by 5, print"buzz"
# - if the value is divisible by  3 and 5, print "fizzbuzz"

num = int(input("enter an upper limit: "))
for i in range(num+1):
    print("number: ",i)
     #if not i % 3: 
    if i % 3 == 0 and i % 5 ==0:
         print("fizzbuzz")
    elif i % 3 == 0 :
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    




          


