import sys
import math

carts = int(sys.stdin.readline())
dust = list(map(int, sys.stdin.readline().split())) #4, 5, 4, 3, 6

carts -= (math.ceil(dust[0]/4.0) + math.ceil(dust[1]/5.0) + math.ceil(dust[2]/4.0) + math.ceil(dust[3]/3.0) + math.ceil(dust[4]/6.0))

if int(carts) > 0:
  print int(carts)
else:
  print 0
