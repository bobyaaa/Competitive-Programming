n = input()
x_list = []
y_list = []

for x in range(n):
  length = input()
  x_list = x_list + raw_input().split()
  y_list = y_list + raw_input().split()
  
  for y in range(length):
    x_list[y] = int(x_list[y])
    y_list[y] = int(y_list[y])
    
  maximum = 0
  
  for y in range(length):
    for z in range(y, length):
      if x_list[y] <= y_list[z] and (z - y) > maximum:
        maximum = (z - y)
        
  print "The maximum distance is " + str(maximum)
  del x_list[:]
  del y_list[:]
