#Soluton by Andrew Xing
dank = raw_input().split()

for x in range(1, len(dank)):
  if dank[x][0].isupper() == True:
    dank[x-1] = dank[x-1] + "."

if dank[len(dank)-1][len(dank[len(dank)-1])-1] == ".":
  pass
else:
  dank[len(dank)-1] = dank[len(dank)-1] + "."
  
print dank[0],

for x in range(1, len(dank)):
  print dank[x],
