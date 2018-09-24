#FINISHED
def smallest_prime_fact(num):
  n = 2
  while num % n != 0:
    n += 1
  return n
  
smallest_prime_fact(2557)