import sys

n = input()
t = input()
dp_but_not_really = [input() for x in range(n)]
dp_but_not_really.sort()

result = 10000

for x in range(t-1, n):
  #Find the minimum of the furthest negative and furthest positive
  #Use it to compute minimum distance
  #If there is only positive, or only negative, then we just use the furthest positive/furthest negative
  #as our distance.
  if dp_but_not_really[x-(t-1)] <= 0 and dp_but_not_really[x] <= 0:
    save = abs(dp_but_not_really[x-(t-1)])
  elif dp_but_not_really[x-(t-1)] >= 0 and dp_but_not_really[x] >= 0:
    save = abs(dp_but_not_really[x])
  else:
    minimum = min(abs(dp_but_not_really[x-(t-1)]), dp_but_not_really[x])
    if minimum == abs(dp_but_not_really[x-(t-1)]):
      save = minimum*2 + dp_but_not_really[x]
    else:
      save = minimum*2 + abs(dp_but_not_really[x-(t-1)])

  if save < result:
    result = save
    
print result
