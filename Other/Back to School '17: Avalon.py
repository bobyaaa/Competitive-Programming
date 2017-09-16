#Solution by Andrew Xing

n = input()
li = []

for x in range(n):
  li.append(list(map(int, raw_input().split())))

total_prob = 1

for x in range(len(li)):
  prob = 1 - (float(li[x][0]) / float(li[x][1]))
  total_prob = total_prob * prob
  
print total_prob
