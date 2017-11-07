#Please excuse my disgusting variable naming.. just pretend 'dank' is a temporary variable just for inputs or something.
#BFS algorithm but BFSing on every possible node in the graph to avoid TLE (instead of BFS on all possible queries).
#Solution by Andrew Xing

import sys

dank = list(map(int, sys.stdin.readline().split())) 
nodes = dank[0] 
edges = dank[1]
time = dank[2]

graph = [[] for x in range(nodes+1)] #Extra index at 0 for conv

for x in range(edges):
  edge = list(map(int, sys.stdin.readline().split()))
  a = edge[0]
  b = edge[1]
  graph[a].append(b)
  
#Ok now let's bfs the graph, no dijkstra's needed

distance = [[9999999 for x in range(nodes+1)] for y in range (nodes+1)]

a = 0
for i in range(nodes): #We're now looking at distance[i]
  a = a+1
  queue = []
  queue.append(a)
  distance[i][a] = 0
  
  visited = [False for j in range(nodes+1)]
  
  while (queue):
    node = queue.pop()
    
    for j in range(len(graph[node])):
      if visited[graph[node][j]] == False:
        distance[i][graph[node][j]] = distance[i][node] + time
        queue.insert(0, graph[node][j])
        visited[graph[node][j]] = True

query = int(sys.stdin.readline())

for x in range(query):
  dank = list(map(int, sys.stdin.readline().split()))
  if distance[dank[0]-1][dank[1]] == 9999999:
    print "Not enough hallways!"
  else:
    print distance[dank[0]-1][dank[1]]
