
left_motor  = "47253470468140030036520"
right_motor = "47248007641358630233090"
back_motorL = "47244882045033290949872"
back_motorR = "47257877708224811671957"
door        = "47248306571744021350642"

IDL         = "51964705888413477303963"
IDR         = "51977360899710284482911"
#line        = "4757420807494607018744"
#limit       = "12345"

S = -0.5

def autonomous_setup():
    Robot.run(go,S)
    print("Running RFID Scanners\nSpeed:",S)


def autonomous_main():
    
    '''
    if Robot.get_value(IDL, "tag_detect") or Robot.get_value(IDR, "tag_detect"):
        if Robot.get_value(ID1, "tag_detect"):
            num = Robot.get_value(IDL, "id")
        else:
            num = Robot.get_value(IDR, "id")
        sol = Robot.decode_message(num)
        print("Attempt Successful: ", sol)
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)
    '''
async def go(s):
    x = -0.5
    
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)
    print("awaiting")
    await Actions.sleep(3.0)
    
    Robot.set_value(left_motor, "duty_cycle", S)
    Robot.set_value(right_motor, "duty_cycle", -S)
    print("start")
    await Actions.sleep(.75)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(.5)
    
    Robot.set_value(left_motor, "duty_cycle", x)
    Robot.set_value(right_motor, "duty_cycle", x)
    print("Turning Right")
    await Actions.sleep(2.0)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward and hit wall")
    await Actions.sleep(5.35)
    
    Robot.set_value(left_motor, "duty_cycle", -x)
    Robot.set_value(right_motor, "duty_cycle", -x)
    print("we goin left bois")
    await Actions.sleep(2.5)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(1.0)
    
    
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle",0)
    print("Stopped")

    '''
    
    Robot.set_value(left_motor, "duty_cycle", -x)
    Robot.set_value(right_motor, "duty_cycle", -x)
    print("Turning Left lEave wall")
    await Actions.sleep(1.75)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(3.0)
    '''
    #while Robot.get_value(limit, "switch0") or Robot.get_value(limit, "switch1") or Robot.get_value(limit, "switch2"):
    '''
    Robot.set_value(left_motor, "duty_cycle", -x)
    Robot.set_value(right_motor, "duty_cycle", -x)
    print("Left")
    await Actions.sleep(1.5)
    '''
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(1.0)
    '''
async def ho(s):
    x = 0.5
    Robot.set_value(left_motor, "duty_cycle", S)
    Robot.set_value(right_motor, "duty_cycle", -S)
    await Actions.sleep(1.0)
    print("start")

    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(1.0)

    Robot.set_value(left_motor, "duty_cycle", -x)
    Robot.set_value(right_motor, "duty_cycle", -x)
    print("Turning Left")
    await Actions.sleep(1.75)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(3.0)

    
    Robot.set_value(left_motor, "duty_cycle", -x)
    Robot.set_value(right_motor, "duty_cycle", -x)
    print("Turning")
    await Actions.sleep(2.5)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(5.0)
    '''
    while Robot.get_value(limit, "switch0") or Robot.get_value(limit, "switch1") or Robot.get_value(limit, "switch2"):
        Robot.set_value(left_motor, "duty_cycle", -x)
        Robot.set_value(right_motor, "duty_cycle", -x)
        print("Pressed Wall")
        await Actions.sleep(1.0)
        
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    print("Forward")
    await Actions.sleep(6.0)

def teleop_setup():
    print("if you travel at the speed of light Things Fall Apart.")

def teleop_main():
    rsticky = Gamepad.get_value("joystick_right_y",0)
    lsticky = Gamepad.get_value("joystick_left_y",0)
    rtrig = Gamepad.get_value("r_trigger", 0)
    ltrig = Gamepad.get_value("l_trigger", 0)
    Upad  = Gamepad.get_value("dpad_up", 0)
    Dpad  = Gamepad.get_value("dpad_down", 0)
    m = 0.5
    
    #Movement
    if (abs(lsticky) > 0.25) or (abs(rsticky) > 0.25):
        Robot.set_value(left_motor, "duty_cycle", lsticky)
        Robot.set_value(right_motor, "duty_cycle",-rsticky)
    
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)
    
    #Velcro Belt
    if rtrig == True:
        Robot.set_value(back_motorL, "duty_cycle", .5)
        Robot.set_value(back_motorR, "duty_cycle", -.5)

    elif ltrig == True:
        Robot.set_value(back_motorL, "duty_cycle", -.5)
        Robot.set_value(back_motorR, "duty_cycle", .5)

    else:
        Robot.set_value(back_motorL, "duty_cycle", 0)
        Robot.set_value(back_motorR, "duty_cycle", 0)
    
    #Door
    if Upad == True:
        Robot.set_value(door, "duty_cycle", m)
    
    elif Dpad == True:
        Robot.set_value(door, "duty_cycle", -m)
    
    else:
        Robot.set_value(door, "duty_cycle", 0)
    
    #Challenge Solver  
    '''
    while Robot.get_value(IDL, "tag_detect") or (Robot.get_value(IDR, "id")):
        if Robot.get_value(IDL, "tag_detect"):
            num = Robot.get_value(IDL, "id")
        else:
            num = Robot.get_value(IDR, "id")
    
    for x in range(1,6):
        sol = Robot.decode_message(x)
        print("Attempt Successful: ", sol)
    '''

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
  return(''.join(num))
 

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
      return binary


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
      return num


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
  return ''.join(SIMD)
  
  
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
  
  return (''.join(map(str, results[::-1])))