win = False
counter = 1

while win == False:
  roll = input()
  if roll == 0:
    break
  
  counter = counter + roll
  
  if counter == 9:
    counter = 34
  elif counter == 40:
    counter = 64
  elif counter == 54:
    counter = 19
  elif counter == 67:
    counter = 86
  elif counter == 90:
    counter = 48
  elif counter == 99:
    counter = 77
  elif counter == 100:
    print "You are now on square " + str(counter)
    win = True
    break
  elif counter > 100:
    counter = counter - roll
  else:
    counter = counter
    
  print "You are now on square " + str(counter)
  
if roll == 0:
  print "You Quit!"
else:
  print "You Win!"
