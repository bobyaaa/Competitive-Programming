#Solution by Andrew Xing
import sys

length = list(map(int, sys.stdin.readline().split())) #n = length[0], m = length[1]
first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

grid = [[0 for x in range(length[0]+1)] for y in range(length[1]+1)] #n will be column, m will be row

for i in range(1, length[1]+1):
  for j in range(1, length[0]+1):
    if first[j-1] == second[i-1]:
      grid[i][j] = grid[i-1][j-1] + 1
    else:
      grid[i][j] = max(grid[i-1][j], grid[i][j-1])
      
print grid[length[1]][length[0]]
