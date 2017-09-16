import sys

def gcd(m,n):
  if n == 0:
    return m
  else:
    return gcd(n, m%n)
    
gundam = sys.stdin.readline().split()

for x in range(3):
  gundam[x] = int(gundam[x])

n = input()
final = set()

for x in range(n):
  enemy = sys.stdin.readline().split()
  for y in range(3):
    enemy[y] = int(enemy[y])
  enemy[0] -= gundam[0]
  enemy[1] -= gundam[1]
  enemy[2] -= gundam[2]
  
  dank = abs(gcd(enemy[0], gcd(enemy[1], enemy[2])))
  
  final.add((enemy[0]/dank, enemy[1]/dank, enemy[2]/dank))

print len(final)
