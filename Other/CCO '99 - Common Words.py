cases = input()

for x in range(cases):
  case = raw_input().split()
  case[0] = int(case[0])
  case[1] = int(case[1])
  
  word_list = []
 
  for x in range(case[0]):
    add = True
    save = [1, raw_input()]
    for y in range(len(word_list)):
      if save[1] == word_list[y][1]:
        word_list[y][0] = word_list[y][0] + 1
        add = False
        break
    if add == True:
      word_list.append(save)

  for x in range(len(word_list)-1,0,-1):
    for y in range(x):
      if word_list[y] < word_list[y+1]:
        word_list[y], word_list[y+1] = word_list[y+1], word_list[y]
  
  if case[1] > case[0]:
    if len(str(case[1])) > 1:
      if str(case[1])[len(str(case[1])) - 2] == "1":
        if str(case[1])[len(str(case[1])) - 1] == "1":
          print str(case[1]) + "th most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "2":
          print str(case[1]) + "th most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "3":
          print str(case[1]) + "th most common word(s):"
      else:
        if str(case[1])[len(str(case[1])) - 1] == "1":
          print str(case[1]) + "st most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "2":
          print str(case[1]) + "nd most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "3":
          print str(case[1]) + "rd most common word(s):"
        else:
          print str(case[1]) + "th most common word(s):"
    else:
      if str(case[1])[len(str(case[1])) - 1] == "1":
        print str(case[1]) + "st most common word(s):"
      elif str(case[1])[len(str(case[1])) - 1] == "2":
        print str(case[1]) + "nd most common word(s):"
      elif str(case[1])[len(str(case[1])) - 1] == "3":
        print str(case[1]) + "rd most common word(s):"
      else:
        print str(case[1]) + "th most common word(s):"
    
  else:
    counter = 1
    save = word_list[0][0]
    common_words = []
    for x in range(len(word_list)):
      if word_list[x][0] != save:
        counter = x + 1
        save = word_list[x][0]
      if counter == case[1]:
        common_words.append(word_list[x][1])
    
    if len(str(case[1])) > 1:
      if str(case[1])[len(str(case[1])) - 2] == "1":
        if str(case[1])[len(str(case[1])) - 1] == "1":
          print str(case[1]) + "th most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "2":
          print str(case[1]) + "th most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "3":
          print str(case[1]) + "th most common word(s):"
      else:
        if str(case[1])[len(str(case[1])) - 1] == "1":
          print str(case[1]) + "st most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "2":
          print str(case[1]) + "nd most common word(s):"
        elif str(case[1])[len(str(case[1])) - 1] == "3":
          print str(case[1]) + "rd most common word(s):"
        else:
          print str(case[1]) + "th most common word(s):"
    else:
      if str(case[1])[len(str(case[1])) - 1] == "1":
        print str(case[1]) + "st most common word(s):"
      elif str(case[1])[len(str(case[1])) - 1] == "2":
        print str(case[1]) + "nd most common word(s):"
      elif str(case[1])[len(str(case[1])) - 1] == "3":
        print str(case[1]) + "rd most common word(s):"
      else:
        print str(case[1]) + "th most common word(s):"
    
    for x in range(len(common_words)): #Frick, I think I screwed up the order of the words with sorting..
      print common_words[x]
        
  print ""
