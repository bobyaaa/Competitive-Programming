n = input()
line = raw_input().split()

print " ".join(line)

for passnum in range(len(line)-1,0,-1):
  for i in range(passnum):
    if int(line[i])>int(line[i+1]):
      line[i], line[i + 1] = line[i + 1], line[i]
      print " ".join(line)
