first = input()
last = input()

if first == last:
  print "All positions change in year " + str(first)
else: 
  for x in range(last - first + 1):
    if x % 60 == 0:
      print "All positions change in year " + str(first + x)
