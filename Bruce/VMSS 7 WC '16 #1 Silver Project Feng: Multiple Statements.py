n = input()
dank = []

for x in range(n):
  danker = input()
  dank.append(danker)

frequency = []
for x in range(n):
  if [dank[x], dank.count(dank[x])] not in frequency:
    frequency.append([dank[x], dank.count(dank[x])])
  
frequency.sort()
  
for x in range(len(frequency)-1, -1, -1):
  if frequency[x][0] == frequency[x][1]:
    print frequency[x][1]
    break
else:
  if 0 in dank:
    print "Paradox!"
  else:
    print 0
