import pygame

# Part A
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
    objs_in_seq.update({n:iteration(n)})
  print(objs_in_seq)
  return objs_in_seq

# Part B
def graphing_iterations(objs_in_seq):
  while 1:
    pygame.event.pump()
    screen = pygame.display.set_mode()
    coordinates = objs_in_seq.items()
    print(coordinates)
    pygame.draw.lines(screen,"blue",True,coordinates)
    new_display = pygame.transform.flip(screen, False, True)

    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))

    screen.blit(new_display, (0, 0))



# --- MAIN CODE ---
def main():
  pygame.init()
  iteration(5)
  iteration_range(20)
  graphing_iterations(10)
  return None 

main()
