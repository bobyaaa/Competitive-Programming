n = input()
dank = raw_input().split()
counter = 0

for x in range(len(dank)):
  if len(dank[x]) <= 10:
    counter += 1

print counter
