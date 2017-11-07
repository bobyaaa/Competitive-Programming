#Plain BFS on a grid.
#Solution by Andrew Xing

import sys

n = int(sys.stdin.readline())

grid = [0 for y in range(52)]

for i in range(n): 
  dimensions = list(map(int, raw_input().split())) 
  col = dimensions[0]
  row = dimensions[1]
  
  for j in range(1, row+1):
    grid[j] = list("X" + sys.stdin.readline())
    
  grid[0] = list("X" * (col+2))
  grid[row+1] = list("X" * (col+2))
  
  for j in range(1, row+1):
    grid[j][col+1] = "X"
    
  #Locate the end point, turn it into 'O' for convinience and save the value
  breaker1 = False
  for y in range(1, row+1):
    for x in range(1, col+1):
      if grid[y][x] == 'W':
        end = [y, x]
        grid[y][x] = 'O'
        breaker1 = True
        break
    if breaker1 == True:
      break
        
        
  #Create distance array and visited array
  
  visited = [[False for x in range(col+2)] for y in range(row+2)]
  distance = [[9999 for x in range(col+2)] for y in range(row+2)]
      
  #What now.. Locate the position of the 'C' and and append it to a queue
  queue = []
  breaker1 = False
  for y in range(1, row+1):
    for x in range(1, col+1): 
      if grid[y][x] == 'C':
        queue.append([y, x])
        distance[y][x] = 0
        breaker1 = True
        break
    if breaker1 == True:
      break
        
  while (queue):
    minimum = 10000
    for i in range(len(queue)):
      if distance[queue[i][0]][queue[i][1]] < minimum:
        minimum = i
    
    node = queue.pop(minimum)
    
    #Now we meme
    if grid[node[0]][node[1]+1] == 'O':
      if visited[node[0]][node[1]+1] == False: 
        queue.append([node[0], node[1]+1])
        visited[node[0]][node[1]+1] = True 
      if distance[node[0]][node[1]] + 1 < distance[node[0]][node[1]+1]:
        distance[node[0]][node[1]+1] = distance[node[0]][node[1]] + 1
          
    if grid[node[0]][node[1]-1] == 'O':
      if visited[node[0]][node[1]-1] == False: 
        queue.append([node[0], node[1]-1])
        visited[node[0]][node[1]-1] = True 
      if distance[node[0]][node[1]] + 1 < distance[node[0]][node[1]-1]:
        distance[node[0]][node[1]-1] = distance[node[0]][node[1]] + 1
  
    if grid[node[0]+1][node[1]] == 'O':
      if visited[node[0]+1][node[1]] == False: 
        queue.append([node[0]+1, node[1]])
        visited[node[0]+1][node[1]] = True 
      if distance[node[0]][node[1]] + 1 < distance[node[0]+1][node[1]]:
        distance[node[0]+1][node[1]] = distance[node[0]][node[1]] + 1
  
    if grid[node[0]-1][node[1]] == 'O':
      if visited[node[0]-1][node[1]] == False: 
        queue.append([node[0]-1, node[1]])
        visited[node[0]-1][node[1]] = True 
      if distance[node[0]][node[1]] + 1 < distance[node[0]-1][node[1]]:
        distance[node[0]-1][node[1]] = distance[node[0]][node[1]] + 1
  
  if distance[end[0]][end[1]] >= 60:
    print "#notworth"
  else:
    print distance[end[0]][end[1]]
