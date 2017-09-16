def factorial(n):
  if n == 1:
    return 1
  elif n == 0:
    return 1
  return factorial(n-1) * n

cases = input()

for x in range(cases):
  dank = input()
  if dank <= 33:
    print factorial(dank) % 2**32
  else:
    print 0
