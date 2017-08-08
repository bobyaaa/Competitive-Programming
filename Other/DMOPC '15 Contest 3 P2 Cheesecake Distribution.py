import sys
n = int(sys.stdin.readline())

cheesecakes = list(map(int, sys.stdin.readline().split()))
cheesecake_sum = sum(cheesecakes)

if cheesecake_sum % len(cheesecakes) != 0:
  print "Impossible"
else:
  perfect = cheesecake_sum / len(cheesecakes)
  result = 0
  for x in range(len(cheesecakes)):
    if cheesecakes[x] > perfect:
      result += cheesecakes[x] - perfect
  print result
