import sys

restrictions = list(map(int, sys.stdin.readline().split()))
cages = restrictions[0]
time = restrictions[1]

chart = [[0 for x in range(time+1)] for y in range(cages+1)]

for x in range(1, cages+1):
  something = list(map(int, sys.stdin.readline().split()))
  princesses = something[0]
  timetaken = something[1]
  
  for y in range(1, time+1):
    if y >= timetaken: #Then we must try out the option
      if princesses + chart[x-1][y-timetaken] > chart[x-1][y]:
        chart[x][y] = princesses + chart[x-1][y-timetaken]
      else:
        chart[x][y] = chart[x-1][y]
    else:
      chart[x][y] = chart[x-1][y]
  
print chart[cages][time]
