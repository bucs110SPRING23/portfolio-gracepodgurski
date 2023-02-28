import random
guess = int(input("Please enter a number between 1-1000: "))
x = random.randrange(1,10)


while guess != x:
    # for count, value in enumerate(values, start=1):
    #  print(count, value)
    if guess < x:
        print("Too Low!")
        guess = int(input("Please enter a number between 1-1000: "))
    elif guess > x:
        print("Too High!")
        guess = int(input("Please enter a number between 1-1000: "))
    elif guess == x: 
        print("correct!!")
    break

print(x)

# for count, value in enumerate(values, start=1):
#         print(count, value)

