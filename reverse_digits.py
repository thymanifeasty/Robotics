#FINISHED
def reverse_digits(num):
  num = [(str(num))[::-1].strip('0')]
  print(''.join(num))
  
reverse_digits(12345)