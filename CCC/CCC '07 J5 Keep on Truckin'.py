# I guess we do it with stack?

hotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

min_distance = input()
max_distance = input()

n = input()

for x in range(n):
  hotels.append(input())

hotels.sort()
stack = []
stack.append(hotels[0])

counter = 0

while len(stack) >= 1:
  save = stack[len(stack)-1]
  stack.pop()
  
  for x in range(1, len(hotels)):
    if hotels[x] >= save + min_distance and hotels[x] <= save + max_distance:
      stack.append(hotels[x])
  
  if len(stack) == 0:
    break
  elif stack[len(stack)-1] == 7000:
    counter += 1

print counter
