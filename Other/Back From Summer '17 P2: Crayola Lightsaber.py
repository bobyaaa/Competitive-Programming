import sys

n = int(sys.stdin.readline())
dank = sys.stdin.readline().split()

red = dank.count("red")
orange = dank.count("orange")
yellow = dank.count("yellow")
green = dank.count("green")
blue = dank.count("blue")
black = dank.count("black")

dank_list = [red, orange, yellow, green, blue, black]

for x in range(6):
  if dank_list[x] > n - dank_list[x]:
    if x == 0:
      #red
      print (orange+yellow+green+blue+black)*2 + 1
    elif x == 1:
      print (red+yellow+green+blue+black)*2 + 1
    elif x == 2:
      print (red+orange+green+blue+black)*2 + 1
    elif x == 3:
      print (red+orange+yellow+blue+black)*2+ 1
    elif x == 4:
      print (red+orange+yellow+green+black)*2 +1
    elif x == 5:
      print (red+orange+yellow+green+blue)*2 + 1
    break
else:
  print n
