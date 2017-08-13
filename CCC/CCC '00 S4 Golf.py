#Ok here's a much more understandable version.
#Basically we try to hit every spot on the field with all of our clubs. Say, we're 39 meters in, and we have 3 clubs (2, 3, 4), we'll
#Then hit the spot at 39 with the 2 club, the 3 club, and the 4 club.
#Each position or spot on the field displays the least amount of hits to get to it. It being 5281 means it cannot be reached.
#If we find a method that requires less strokes to get to the same spot, then we'll replace the existing number at that spot
#with the smaller number. So if we're on spot 39 (and it took us like 12 hits or something), and we decide to hit the ball 
#with a 4 meter club, and the DP chart says it takes 5281 hits (impossible) to get to spot 43, then we'll just replace 5281 with
#(12+1) because it's smaller.
#
#Solution by Andrew Xing

distance = input()
clubs = [input() for x in range(input())] 
least = [5281 for x in range(distance+1)]
least[0] = 0

for i in range(distance+1):
  for j in range(len(clubs)):
    if i + clubs[j] <= distance: #If it doesn't go past
      if least[i] + 1 < least[i+clubs[j]]:
        least[i+clubs[j]] = least[i] + 1
  
if least[distance] < 5281:
  print "Roberta wins in " + str(least[distance]) + " strokes."
else:
  print "Roberta acknowledges defeat."
