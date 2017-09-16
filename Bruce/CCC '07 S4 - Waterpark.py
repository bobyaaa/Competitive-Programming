import sys
n = int(sys.stdin.readline())

adj = [[] for x in range(n+1)]
dp = [0 for x in range(n+1)]
dp[n] = 1

while True:
  dank = list(map(int, sys.stdin.readline().split())) 
  if dank[0] == 0:
    break
  adj[dank[1]].append(dank[0]) #Shifted one unit to the right

for i in range(n, -1, -1):
  for j in range(len(adj[i])):
    dp[adj[i][j]] += dp[i]
    #print dp
    
print dp[1]
