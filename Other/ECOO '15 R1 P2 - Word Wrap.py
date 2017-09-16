counter = 0

while counter != 10: 
  n = input()
  string = raw_input().split()
  
  length =  0
  concatentated = ""
  
  #ok, how about instead of this complete crapstorm, we'll split the words beforehand and add them to a new list.
  
  new_list = []
  
  for x in range(len(string)):
    if len(string[x]) > n:
      new_list.append(string[x][:n])
      cut = string[x][n:]
      for y in range(len(string[x]) / n):
        if cut == "":
          break
        else:
          new_list.append(cut[:n])
          cut = cut[n:]
    else:
      new_list.append(string[x])
  
  for x in range(len(new_list)):
    if len(concatentated) + len(new_list[x]) <= n:
      concatentated = concatentated + new_list[x] + " "
    else:
      print concatentated
      if len(new_list[x]) >= n:
        print new_list[x][:n]
        concatentated = new_list[x][n:]
      else:
        concatentated = new_list[x] + " "
  
  if concatentated != " ":
    print concatentated
  counter = counter + 1
  
  print "====="
