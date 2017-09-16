def recursion_sucks(n):
  heh = 0
  for x in range(1, n + 1):
    heh = heh + x
  return heh
  
li = raw_input().split()

n_stops = int(li[0])
n_rocket_stops = int(li[1]) #What if it is zero?
n_passengers = int(li[2])

if n_rocket_stops != 0:
  rocket_stops = raw_input().split()
  passengers = raw_input().split()

  if n_passengers % 2 == 0:
    need = n_passengers / 2
  else:
    need = (n_passengers + 1) / 2
    
  counter = 0
  
  for x in range(n_passengers):
    if passengers[x] in rocket_stops:
      if counter != need:
        counter = counter + 1
      
  print recursion_sucks(counter) + recursion_sucks(n_passengers - counter)
  
else:
  print recursion_sucks(n_passengers)
