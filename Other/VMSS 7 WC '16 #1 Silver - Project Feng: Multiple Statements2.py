#Basically, if an input number occurs as many times as its value (ex: 2 appears twice in the input list), then it is a viable solution because there would be n correct statements, and since n also the number of solutions, it prouves itself true. 
#Solution by Andrew Huang

statements = []
viable_answers = []
n = input()

#This stores the input of numbers after the first as a list of numbers
for x in range(n):
  statements.append(input())

#Finds viable solutions (where the count of the number is equal to the number itself)
for x in range(max(statements)+1):
  if statements.count(x)==x:
    viable_answers.append(x)

#Looks at the viable answers (or lack thereof) and prints the suitable result. 
#Note: Having zero in the input can lead to a paradox, but only if there are no other viable solutions.
if len(viable_answers)>0:
  print max(viable_answers)
elif li.count(0)!=0 and len(viable_answers)==0:
  print 'Paradox!'
else:
  print 0

