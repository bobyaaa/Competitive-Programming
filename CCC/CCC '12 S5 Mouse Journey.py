#Finding maximum amount of routes without cat, so we gotta make this grid counter thing (math)
#Not dynamic programming solution, but some clever counting involved.
#Since this is one of my earlier submissions (1 week after starting to code), it's kinda sketchy. But the method works like a Boolean
board with XOR function with a hint of I don't really remember too much.

dimensions = raw_input().split()
for x in range(2):
  dimensions[x] = int(dimensions[x])

row = dimensions[0]
col = dimensions[1]

box = [[] for x in range(row)]

for x in range(row):
  for y in range(col):
    box[x].append(1)

#Inputing cage coordinates

cats = input()
cage_coords = []
for x in range(cats):
  cage_coords.append(raw_input().split())

for x in range(len(cage_coords)):
  cage_coords[x][0] = int(cage_coords[x][0])
  cage_coords[x][1] = int(cage_coords[x][1])

#Toss in the zeros.

for x in range(len(cage_coords)):
  box[cage_coords[x][0] - 1][cage_coords[x][1] - 1] = 0 
  #Write in left side no overwrite
  if cage_coords[x][1] == 1:
    for y in range(cage_coords[x][0], row):
      box[y][0] = 0
  elif cage_coords[x][0] == 1:
    for y in range(cage_coords[x][1], col):
      box[0][y] = 0
#Diagonal calculations and exceptions.

for x in range(1, row):
  for y in range(1, col):
    if box[x][y] != 0: #Make sure you don't overwrite zeros
      box[x][y] = box[x-1][y] + box[x][y-1]

max_route = box[row-1][col-1]

print max_route
