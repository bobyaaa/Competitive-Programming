height = input()
space = input()
handle = input()


for x in range(height):
  print "*" + space * " " + "*" + space * " " + "*"
  
print (space*2 + 3)*"*"

for x in range(handle):
  print (space+1)*" " + "*" + (space+1) * " "
