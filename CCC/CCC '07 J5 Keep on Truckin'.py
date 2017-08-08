# I guess we do it with stack?
# Yeah, we'll do it with stack. We're going to count how many times the top value of the stack reaches 7000. 
# If a hotel falls into the range of the minimum distance and the maximum distance from a hotel before, 
# append it to the stack (can be more than one). Remove one hotel from the stack each loop, but save the value to find if there is any
# hotels in front of it. Loop breaks when the stack is empty

# Solution by Andrew Xing

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
