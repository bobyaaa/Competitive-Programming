#Input
graph1 = {'A': [],
         'B': [],
         'C': [],
         'D': [],
         'E': [],
         'F': [],
         'G': [],
         'H': [],
         'I': [],
         'J': [],
         'K': [],
         'M': [],
         'O': [],
         'P': [],
         'Q': [],
         'R': [],
         'S': [],
         'T': [],
         'U': [],
         'V': [],
         'W': [],
         'X': [],
         'Y': [],
         'Z': []
}

reverse = []

isDone = False
while isDone == False:
  temp = raw_input()
  temp1 = temp[::-1]
  if temp == "**":
    isDone = True
  else: 
    reverse.append(temp1)
    for key in graph1:
      if temp[0] == key:
        graph1[key] = graph1[key] + list(temp[1])
      if temp1[0] == key:
        graph1[key] = graph1[key] + list(temp1[1])
        
def find_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  for node in graph[start]:
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath: return newpath #This is wierd
  return 0
  
counter = 0

for key in graph1:
  for item in range(len(graph1[key])):
    save = graph1[key][item]
    graph1[key].pop(item)
    if find_path(graph1, "A", "B") == 0:
      graph1[key].insert(0, save)
      almost_answer = key + save
      if almost_answer in reverse:
        print almost_answer[::-1]
      else:
        print almost_answer
      counter = counter + 1
    else:
      graph1[key].insert(0, save)
  
print "There are " + str(counter) + " disconnecting roads."
