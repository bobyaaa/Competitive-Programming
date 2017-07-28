dice1 = input()
dice2 = input()

total = 0
fails = 0

for x in range(dice1):
  for y in range(dice2):
    if x+y == 10:
      total += 1
    else: 
      fails +=1
      
if total == 1: 
  print 'There are '+ str(total) + ' ways to get the sum 10.'
else:
  print 'There is '+ str(total) + ' way to get the sum 10.'
