#FINISHED
def next_power(num):
  n = 0
  while num > 2**n:
    n += 1
    
  return (2**n)
  
print(next_power(7132645))