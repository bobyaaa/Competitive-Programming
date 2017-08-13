#Some sketchy calendar right here.
#I think this would be easier in C++ 
#Solution by Andrew Xing

print "Sun Mon Tue Wed Thr Fri Sat"

n = raw_input().split()
li = []

for x in range(int(n[0]) - 1):
   li.append(" ")
  
days = int(n[1])
counter = 1

while counter != days +1:
  li.append(counter)
  counter = counter + 1
  
li1 = "  "

for x in range(len(li)):
  if len(li1) >= 27:
    print li1
    if len(str(li[x])) == 2:
      li1 = " "
    else:
      li1 = "  "
    
  if li[x] == 9:
    li1 = li1 + str(li[x]) + "  "
  elif len(str(li[x])) == 1:
    li1 = li1 + str(li[x]) + "   "
  elif len(str(li[x])) >= 2:
    li1 = li1 + str(li[x]) + "  "

print li1
