def iteration(n):
    count = 0
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
        count = count + 1
       else:
        n = int(3 * n + 1)
        count = count + 1
    
    print("The loop was executed ", count, "times. ")
    return None

def main():
  iteration(25)

main()
