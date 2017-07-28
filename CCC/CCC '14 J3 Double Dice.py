#Solution by Andrew Xing

number = input()
first_list = []
second_list = []
Antonia = 100
David = 100 

for x in range(number):
  first, second = raw_input().split()
  first_list.append(int(first))
  second_list.append(int(second))
  
for y in range(number):
  if first_list[y] > second_list[y]:
    David = David - first_list[y]
  elif first_list[y] < second_list[y]:
    Antonia = Antonia - second_list[y]
    

print Antonia
print David
