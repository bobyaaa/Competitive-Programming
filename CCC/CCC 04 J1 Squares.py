Area = input()

import math

sqrtarea = math.sqrt(Area)

if sqrtarea.is_integer() == True:
  print "The largest square has side length " + str(int(sqrtarea)) + "."
else:
  for x in range(Area):
    Otherarea = Area - x - 0.0
    if Otherarea.is_integer() == True:
      print "The largest square has side length " + str(int(math.sqrt(Otherarea))) + "."
      break
