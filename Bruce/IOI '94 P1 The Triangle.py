import sys
n = int(sys.stdin.readline())

triangle = []
for x in range(n):
  triangle.append(list(map(int, sys.stdin.readline().split())))
  triangle[x].append(0)
  triangle[x].insert(0, 0)
  
#If it's not an edge of the triangle, compare and see which value is better

for x in range(1, n):
  for y in range(1, len(triangle[x])-1):
    if triangle[x][y] + triangle[x-1][y] > triangle[x][y] + triangle[x-1][y-1]: #If right is greater than left
      triangle[x][y] += triangle[x-1][y]
    else:
      triangle[x][y] += triangle[x-1][y-1]

result = 0      #Finding the largest value at the bottom, we're lucky the input doesn't have any negatives.
for x in range(len(triangle[n-1])):
  if triangle[n-1][x] > result:
    result = triangle[n-1][x]
    
print result
