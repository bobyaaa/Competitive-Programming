#AC with pypy2, TLE with python
import sys
gates = int(sys.stdin.readline())
planes = int(sys.stdin.readline())

airport = [0 for x in range(gates)]
result = 0

for x in range(planes):
  plane = int(sys.stdin.readline()) - 1
    
  while plane >= 0 and airport[plane] > 0:
    save = airport[plane]
    airport[plane] += 1
    plane = plane - save
  
  if plane < 0:
    break
  else:
    airport[plane] += 1
    result += 1
    
print result
