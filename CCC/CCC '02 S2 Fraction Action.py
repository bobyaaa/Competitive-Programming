num = input()
dem = input()

counter = 0

if num % dem == 0:
  print num / dem
  
elif num % dem != 0:
  
  for x in range(num):
    num = num - dem
    counter = counter + 1
     
    if num < 0:
      num = num + dem
      counter = counter - 1
      recordednum = num
  
  for x in range(num):
    if (num) % (num - x) == 0 and (dem) % (num - x) == 0:
      num = num / (recordednum - x)
      dem = dem / (recordednum - x)
      
      if counter == 0:
        print str(num) + "/" + str(dem)
        break
      else:
        print str(counter) + " " + str(num) + "/" + str(dem)
        break
