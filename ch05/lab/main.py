import pygame

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
    return count

def iteration_range(upper_limit):
  objs_in_seq = {}
  for n in range(2,upper_limit+1):
    iteration(upper_limit)
    objs_in_seq.update({count:upper_limit})
  return objs_in_seq


def main():
  pygame.init()
  # iteration(25)
  iteration_range(20)
  print(objs_in_seq)
  return None 

main()
