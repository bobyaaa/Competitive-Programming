#Dijkstra's
#By Andrew Xing

def find_min(li):
  minumum = 1000000
  for x in range(len(li)):
    if li[x][1] < minumum:
      minumum = li[x][1]
      save = x
      
  return save

import sys
s = list(map(int, sys.stdin.readline().split()))
n = s[0]
m = s[1]

adj = [[] for x in range(n+1)]
for i in range(m):
  t = list(map(int, sys.stdin.readline().split()))
  adj[t[0]].append([t[1],t[2]])
  adj[t[1]].append([t[0],t[2]])
  
minimum = [1000000 for x in range(n+1)]
minimum[1] = 0
visited = [False for x in range(n+1)]
queue = []
queue.append([1, 0])

while len(queue) > 0:

  temp = queue.pop(find_min(queue))
  visited[temp[0]] = True
  
  for x in range(len(adj[temp[0]])):
    if visited[adj[temp[0]][x][0]] == False:
      if temp[1] + adj[temp[0]][x][1] < minimum[adj[temp[0]][x][0]]:
        minimum[adj[temp[0]][x][0]] = adj[temp[0]][x][1] + temp[1]
        queue.append([adj[temp[0]][x][0], minimum[adj[temp[0]][x][0]]])

for x in range(1, n+1):
  if minimum[x] == 1000000:
    print -1
  else:
    print minimum[x]
