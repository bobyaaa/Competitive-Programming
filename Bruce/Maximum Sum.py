#Solution by Andrew Xing

n = int(input())

dank = [int(input()) for x in range(n)]

if len(dank) < 3:
  print(max(dank))
elif len(dank) == 3:
  dank[2] += dank[0]
  print(max(dank))
else:
  dank[2] += dank[0]
  
  for i in range(3,n):
    dank[i] += max(dank[i-2], dank[i-3])
    
  print(max(dank))
