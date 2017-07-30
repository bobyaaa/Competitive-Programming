#Small syntax errors are mean ;-; 
#So the basic concept is, if the number is in the mountain, pop() and chuck it in the lake
#if the number (ascending) is not in the mountain, check the branch. If it's in the branch, pop() the branch and then put the
#item in the mountain on top of the branch, if it's not in the branch just put the item in the mountain down to the branch.

import sys

n = int(sys.stdin.readline())

for x in range(n):
  m = int(sys.stdin.readline())
  
  mountain = []
  branch = []
  result = "Y"
  
  for x in range(m):
    mountain.append(int(sys.stdin.readline()))
    
  while mountain[len(mountain)-1] != 1:
    branch.append(mountain[len(mountain)-1])
    mountain.pop()
    
  mountain.pop() #Getting rid of the "one" value and throwing it in the lake first will always work
  
  need = 2
  
  while len(mountain) > 0 or len(branch) > 0:
    if len(branch) > 0 and len(mountain) > 0:
      if branch[len(branch)-1] == need:
        branch.pop()
        need += 1
      elif mountain[len(mountain)-1] == need:
        mountain.pop()
        need += 1
      else: #We can't do anything else, so we shove the mountain into the branch
        branch.append(mountain[len(mountain)-1])
        mountain.pop()
    elif len(branch) > 0: #If only the branch has elements in it
      if branch[len(branch)-1] == need:
        branch.pop()
        need += 1
      else: #The candies will not be put into the lake in order, so the result is no and we break
        result = "N"
        break
    else: #If only the mountain has elements in it and nothing in the branch
      if mountain[len(mountain)-1] == need:
        mountain.pop()
        need += 1
      else:
        branch.append(mountain[len(mountain)-1])
        mountain.pop()

  print result
