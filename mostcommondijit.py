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

print(most_common_digit(872164398999796963456761345))