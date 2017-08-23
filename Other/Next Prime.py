//Use xrange() if you ever have break. range() pre-creates the list and that can be memory inefficieint.
//The code below is a bit ugly because I used some measures to optimize it.
//Solution by Andrew Xing

n = input()
breaker = False

if n == 1 or n == 2:
  print 2
elif n == 3:
  print 3
elif n == 5 or n == 4:
  print 5
else:
  for x in xrange(n, n*2):
    if breaker == True:
      break
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
      continue
    else:
      for y in xrange(2, int(x**0.5)):
        if x % y == 0:
          break
      else:
        print x
        breaker = True
