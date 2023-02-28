import random
guess = int(input("Please enter a number between 1-1000: "))
x = random.randrange(1,10)

count = []

while guess != x:
    n = 1
    if guess < x:
        print("Too Low!")
        n = n + 1
        count.append([n])
        guess = int(input("Please enter a number between 1-1000: "))
    elif guess > x:
        print("Too High!")
        n = n + 1
        count.append([n])
        guess = int(input("Please enter a number between 1-1000: "))

if guess == x: 
    print("correct!!")

print(x)
print(count)

# still trying to figure out how to do the enumerate thing...

    # def my_enumerate(guess, start=0):
    #  n = start
    #  for elem in sequence:
    #      yield n, elem
    #      n += 1
    # for count, value in enumerate(values, start=1):
    #  print(count, value)