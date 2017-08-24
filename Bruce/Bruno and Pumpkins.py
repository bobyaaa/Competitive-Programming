#Solution by Andrew Xing
import sys

n = input()
t = input()
dp_but_not_really = [input() for x in range(n)]
dp_but_not_really.sort()
#We sort our dp. This is because we just want to find the optimal solutions. Say we have -4 -3 -2 1 8. Why would you try
#to compute the distance (if you want three pumpkins) for -4, -3, 1, when clearly -4, -3, -2, will give you a better answer.
#All the optimal answers come from indexes subsequent to one another. So like (-4, -3, -2), (-3, -2, 1), (-2, 1, 8). 
#Those are the only things we need to check, and we can run this in O(N) time.

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
