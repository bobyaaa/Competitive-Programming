n = input()
piece = list(map(int, raw_input().split()))

danker = [-999999 for x in range(n+1)]
danker[0] = 0

for x in range(n):
  for y in range(3):
    if x + piece[y] <= n:
      if danker[x] + 1 > danker[x + piece[y]]:
        danker[x + piece[y]] = danker[x] + 1

print danker[n]
