left_motor  = "47253470468140030036520"
right_motor = "47248007641358630233090"
back_motorL = "47249899637113430724572"
back_motorR = "47258416584374622758504"
door        = "47248306571744021350642"

IDL         = "12345"
IDR         = "51965061596721995018468"
line        = "4757420807494607018744"
limit       = "12345"

def autonomous_setup():
    pass

s = 0.5

def autonomous_main():
    Robot.set_value(back_motorL, "duty_cycle", 0.5)
    Robot.set_value(back_motorR), "duty_cycle", -0.5)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    
    Robot.run(go,s)
    '''
    while (Robot.is_running(left) or Robot.is_running(right))  == True:
        
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
    if Robot.get_value(line, "right"):
        s = -s
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", s)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", s)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", -s)
    Robot.set_value(right_motor, "duty_cycle", s)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", 0)
    Robot.set_value(right_motor, "duty_cycle", 0)
    #Robot.set_value(door, "duty_cycle", 0.5)
    await Actions.sleep(0.1)
    #Robot.set_value(door, "duty_cycle", 0)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", -s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    await Actions.sleep(1.0)
    
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    await Actions.sleep(1.0)
    '''
    while Robot.get_value(limit, "switch0") or Robot.get_value(limit, "switch1") or Robot.get_value(limit, "switch2"):
        Robot.set_value(left_motor, "duty_cycle", -s)
        Robot.set_value(right_motor, "duty_cycle", -s)
        await Actions.sleep(1.0)
    '''
    Robot.set_value(left_motor, "duty_cycle", s)
    Robot.set_value(right_motor, "duty_cycle", -s)
    
    
    
    
'''    
async def open_loop_drive():
    
    # Drive forward for one second
    Robot.set_value(left_motor, "duty_cycle", 1.0)
    Robot.set_value(right_motor, "duty_cycle", -1.0)
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
'''

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("if you travel at the speed of light you become light")

def teleop_main():
    rsticky = -Gamepad.get_value("joystick_right_y",0)
    lsticky = -Gamepad.get_value("joystick_left_y",0)
    rtrig = Gamepad.get_value("r_trigger", 0)
    ltrig = Gamepad.get_value("l_trigger", 0)
    Upad  = Gamepad.get_value("dpad_up", 0)
    Dpad  = Gamepad.get_value("dpad_down", 0)
    
    #Movement
    if (abs(lsticky) > 0.25) or (abs(rsticky) > 0.25):
        Robot.set_value(left_motor, "duty_cycle", lsticky)
        Robot.set_value(right_motor, "duty_cycle",-rsticky)
    
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        Robot.set_value(right_motor, "duty_cycle", 0)
    
    #Velcro Belt
    if rtrig == True:
        Robot.set_value(back_motorL, "duty_cycle", .25)
        Robot.set_value(back_motorR, "duty_cycle", -.25)
    else:
        Robot.set_value(back_motorL, "duty_cycle", 0)
        Robot.set_value(back_motorR, "duty_cycle", 0)
    
    #Door
    if Upad == True:
        Robot.set_value(door, "duty_cycle", 0.5)
    
    elif Dpad == True:
        Robot.set_value(door, "duty_cycle", -0.5)
    
    else:
        Robot.set_value(door, "duty_cycle", 0)
     
    #Challenge Solver  
    '''
    if Robot.get_value(ID, "tag_detect"):
        num = Robot.get_value(ID, "id")
    '''   
    if ltrig == True:
        sol = Robot.decode_message(1)
        print("Attempt Successful: ", sol)


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