#Solution by Andrew Xing

quarters = input()

one = input()
two = input()
three = input()

counter = 0

while quarters > 0:
  quarters = quarters - 1
  counter = counter + 1
  one = one + 1
  if one == 35:
    quarters = quarters + 30
    one = 0
  if quarters == 0:
    break
  
  quarters = quarters - 1
  counter = counter + 1
  two = two + 1
  if two == 100:
    quarters = quarters + 60
    two = 0
  if quarters == 0:
    break
  
  quarters = quarters - 1
  counter = counter + 1
  three = three + 1
  if three == 10:
    quarters = quarters + 9
    three = 0
  if quarters == 0:
    break
  
print "Martha plays "+ str(counter)+" times before going broke."
