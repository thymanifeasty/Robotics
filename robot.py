left_motor = "47258416584374622758504"
right_motor = "47248007641358630233090"
back_motorL = "12345"
back_motorR = "12345"

def autonomous_setup():
    Robot.run(open_loop_drive)

def autonomous_main():
    pass

async def open_loop_drive():
    
    # Drive forward for one second
    Robot.set_value(left_motor, "duty_cycle", 1.0)
    Robot.set_value(right_motor, "duty_cycle", 1.0)
    await Actions.sleep(1.0)

    # Turn right for half a second
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(0.5)

    # Drive forward again
    Robot.set_value(left_motor, "duty_cycle", 1.0)
    Robot.set_value(right_motor, "duty_cycle", 1.0)
    await Actions.sleep(0.5)
#right
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(0.5)
#for
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(0.5)
    
#back
    Robot.set_value(left_motor, "duty_cycle", -1)
    Robot.set_value(right_motor, "duty_cycle", 1)
    await Actions.sleep(1)
   #180 turn may use later
    Robot.set_value(left_motor, "duty_cycle", -0.5)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    await Actions.sleep(1)
    
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(0.5)
    
    
    


    # Stop
    Robot.set_value(left_motor, "duty_cycle", 0.0)
    Robot.set_value(right_motor, "duty_cycle", 0.0)

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("if you travel at the speed of light you become light")

def teleop_main():
    if Gamepad.get_value("joystick_right_y") > 0.5:
        Robot.set_value(left_motor, "duty_cycle", 1.0)
        Robot.set_value(right_motor, "duty_cycle", -1.0)
        
    elif Gamepad.get_value("joystick_right_y") < -0.5:
        Robot.set_value(left_motor, "duty_cycle", -1.0)
        Robot.set_value(right_motor, "duty_cycle", 1.0)
    elif Gamepad.get_value("joystick_right_x") > 0.5:
        Robot.set_value(left_motor, "duty_cycle", 1.0)
        Robot.set_value(right_motor, "duty_cycle", 1.0)
    elif Gamepad.get_value("joystick_right_X") < -0.5:
        Robot.set_value(left_motor, "duty_cycle", -1.0)
        Robot.set_value(right_motor, "duty_cycle", -1.0)
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)



def next_power(num):
  n = 0
  while num > 2**n:
    n += 1
    
  return (2**n)
  
print(next_power(7132645))

def reverse_digits(num):
  num = [(str(num))[::-1].strip('0')]
  print('b'.join(num))
  

def smallest_prime_fact(num):
  n = 2
  while num % n != 0:
    n += 1
  return n
  
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
      return num
    
print(valid_isbn_ten(12345))

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
  return ''.join(SIMD)

print(simd_four_square(4))