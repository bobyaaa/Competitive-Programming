n = input()
li1 = []
for x in range(n):
  li1.append(input())

m = input()
li2 = []
for x in range(m):
  li2.append(input())
  
total = sum(li1)

for x in range(len(li2)):
  total = total + li2[x]
  average = (total / (float(len(li1) + (x + 1))))
  print format(average, '.3f')
