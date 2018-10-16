###########################
# Solar Scramble Functions 
###########################   

#Next Power
def next_power(num):
  n = 0
  while num > 2**n:
    n += 1
  return (2**n)


#Reverse Digits
def reverse_digits(num):
  num = [(str(num))[::-1].strip('0')]
  return int(''.join(num))
 

#Smallest Prime Factor
def smallest_prime_fact(num):
  n = 2
  while num % n != 0:
    n += 1
  return n
  

#Silly Base Two    
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
      return int(binary)


#Most Common Digit  
def most_common_digit(num):
  x = sorted(list(str(num)))
  print(x)
  Moccur = x[0]
  Check = x[0]
  Mcounter = 0
  Ccounter = 0
  
  for n in range(len(x)):
    if x[n] == Check and n != len(x)-1:
      Ccounter += 1

    else:
      if Ccounter >= Mcounter:
        Mcounter = Ccounter
        Moccur = x[n-1]
      Ccounter = 1
      Check = x[n]
  return Moccur


#Valid ISBN Ten
def valid_isbn_ten(num):
  while True:
    num= list(str(num))
    ISBN = []
    for i in range(1,len(num)+1):
      ISBN.append(int(num[-i])*i)
    
    num = int(''.join(num))
    if sum(ISBN) % 11 != 0:
      num += 1
    else:
      return int(num)


#SIMD Four Square
def simd_four_square(num):
  
  num= list(str(num))
  while len(num)%4 != 0:
    num.insert(0,'0')
    print(num)
    
  square = []
  SIMD=[]
  n = 0
  end= (len(num)//4)
  while n < 4:
    square.append(list(str(int(''.join(num[n*end:(end*n)+end]))**2)))
    SIMD.append(square[n][-(end):])
    SIMD[n] = ''.join(SIMD[n])
    n+=1
  return int(''.join(SIMD))
  
  
#Double Ceasar Cipher    
def double_caesar_cipher(key):
  message = [3,1,4,1,5,9,2,6,5,3]
  num = [int(x) for x in str(key)]
  results = []
  n = 1
  k = 1
  while 10 >= n:
    result = message[-n]+num[-k]
    if result >= 10:
      result = result % 10
    results.append(result)
    if k == len(num):
      k = 0
    n += 1
    k += 1
  
  return int(''.join(map(str, results[::-1])))                      fad