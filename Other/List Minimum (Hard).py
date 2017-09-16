how_many = int(input())

phat_list = []

for x in range(how_many):
  new_thing = input()
  phat_list.append(new_thing)
  
phat_list.sort()

for y in range(len(phat_list)):
  print phat_list[y]
