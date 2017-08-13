low = input()
high = input()

RSA = 0

for x in range(low, high + 1):
  
  counter = 0 
  
  for y in range(1, high + 1):
    if x % y == 0:
      counter = counter + 1
  
  if counter == 4:
      RSA = RSA + 1
    
      
print "The number of RSA numbers between " + str(low) + " and " + str(high) + " is " + str(RSA)
