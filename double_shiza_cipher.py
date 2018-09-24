#FINISHED
def double_caesar_cipher(num):
  message = [3,1,4,1,5,9,2,6,5,3]
  key = [int(x) for x in str(num)]
  results = []
  n = 1
  k = 1
  while 10 >= n:
    result = message[-n]+key[-k]
    if result >= 10:
      result = result % 10
    results.append(result)
    if k == len(key):
      k = 0
    n += 1
    k += 1
  
  return (''.join(map(str, results[::-1])))

print(double_caesar_cipher(1))