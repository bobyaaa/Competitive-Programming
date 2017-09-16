n = input()

li = raw_input().split()
smallest_x = int(li[0])
smallest_y = int(li[1])
largest_x = int(li[0])
largest_y = int(li[1])

for x in range(1, n):
  li = raw_input().split()
  if int(li[0]) <= smallest_x:
    smallest_x = int(li[0])
  elif int(li[0]) >= largest_x:
    largest_x = int(li[0])
  
  if int(li[1]) <= smallest_y:
    smallest_y = int(li[1])
  elif int(li[1]) >= largest_y:
    largest_y = int(li[1])

print (largest_x - smallest_x) * (largest_y - smallest_y)
