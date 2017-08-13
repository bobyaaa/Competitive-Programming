adj = input()
noun = input()

adjliszt = []
nounliszt = []

for x in range(adj):
  adjliszt.append(raw_input())
  
for x in range(noun):
  nounliszt.append(raw_input())
  
for x in range(len(adjliszt)):
  for y in range(len(nounliszt)):
    print adjliszt[x] + " as " + nounliszt[y]
