#FINISHED
def silly_base_two(num):
  binary = []
  n = 0
  while True:
    if num % 2**(n+1) != 0:
      binary.append(1)
      num = num - (2**n)
    else:
      binary.append(0)
    n += 1
    
    if num == 0:
      binary = ''.join(map(str, binary[::-1]))
      return binary

print (silly_base_two(1234))