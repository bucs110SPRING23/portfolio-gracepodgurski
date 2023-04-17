import random
guess = int(input("Please enter a number between 1-10: "))
x = random.randrange(1,11)

for s in range(2):
    if guess < x:
        print("Too Low!")
        guess = int(input("Please enter a number between 1-10: "))
    elif guess > x:
        print("Too High!")
        guess = int(input("Please enter a number between 1-10: "))
    elif guess == x: 
        print("correct!!")
        break

print(x)

