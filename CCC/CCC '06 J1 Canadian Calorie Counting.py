#Tedious tedious lemon tedious
#Solution by Andrew Xing

First = input()
Second = input()
third = input()
fourth = input()

sum = 0 

if First == 1:
  sum = sum + 461
elif First == 2:
  sum = sum + 431
elif First == 3:
  sum = sum + 420
elif First == 4:
  sum = sum
  
if Second == 1:
  sum = sum + 100
elif Second == 2:
  sum = sum + 57
elif Second == 3:
  sum = sum + 70
elif Second == 4:
  sum = sum
  
if third == 1:
  sum = sum + 130
elif third == 2:
  sum = sum + 160
elif third == 3:
  sum = sum + 118
elif third == 4:
  sum = sum
  
if fourth == 1:
  sum = sum + 167
elif fourth == 2:
  sum = sum + 266
elif fourth == 3:
  sum = sum + 75
elif fourth == 4:
  sum = sum
  
print "Your total Calorie count is " + str(sum) + "."
