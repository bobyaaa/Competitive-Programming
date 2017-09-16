import sys
dank = list(map(int, sys.stdin.readline().split())) 
n = dank[0]
m = dank[1]
a = dank[2]
b = dank[3]

adj = [[] for i in range(n+1)]
visited = []
stack = []
poopoo = False

for x in range(m):
  new_meme = list(map(int, sys.stdin.readline().split()))
  adj[new_meme[0]].append(new_meme[1])
  adj[new_meme[1]].append(new_meme[0])
  
for x in range(len(adj[a])):
  stack.append(adj[a][x])

while (len(stack) > 0):
  save = stack[0]
  if save == b:
    poopoo = True
    break
  
  stack.pop(0)
  visited.append(save)
  
  for x in range(len(adj[save])):
    if adj[save][x] not in visited:
      stack.append(adj[save][x])

if a == b:
  print "GO SHAHIR!"
elif poopoo == True:
  print "GO SHAHIR!"
else:
  print "NO SHAHIR!"
