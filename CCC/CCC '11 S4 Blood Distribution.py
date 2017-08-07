have = (raw_input().split())
need = (raw_input().split())

for x in range(8):
  have[x] = int(have[x])
  need[x] = int(need[x])
  
extroN = 0
extroP = 0
extraN = 0
extraP = 0
extrbN = 0
extrbP = 0
extrabN = 0
extrabP = 0
result = 0 

for x in range(8):
  if have[x] >= need[x]:
    if x == 0:
      result = result + need[x]
      extroN = have[x] - need[x]
    elif x == 1:
      result = result + need[x]
      extroP = have[x] - need[x]
    elif x == 2:
      result = result + need[x]
      extraN = have[x] - need[x]
    elif x == 3:
      result = result + need[x]
      extraP = have[x] - need[x]
    elif x == 4:
      result = result + need[x]
      extrbN = have[x] - need[x]
    elif x == 5:
      result = result + need[x]
      extrbP = have[x] - need[x]
    elif x == 6:
      result = result + need[x]
      extrabN = have[x] - need[x]
    elif x == 7:
      result = result + need[x]
      extrabP = have[x] - need[x]
  else:
    if x == 0:
      result = have[x]
    elif x == 1:
      have[x] = have[x] + extroN
      if have[x] > need[x]:
        extroN = have[x] - need[x]
        result = result + need[x]
      else:
        extroN = 0
        result = result + have[x]
    elif x == 2: #This is type A negative, it can use A- and O- 
      have[x] = have[x] + extroN
      if have[x] >= need[x]:
        result = result + need[x]
        if have[x] - need[x] >= extroN:
          extraN = have[x] - need[x] + extroN
        else:
          extroN = have[x] - need[x]
          extraN = 0
      else:
        extroN = 0
        extraN = 0
        result = result + have[x]
    elif x == 3: #This is type A positive, it can use A-, A+, O-, O+ 
      have[x] = have[x] + extraN + extraP + extroN + extroP
      if have[x] >= need[x]:
        result = result + need[x]
        #Code that distributes the extra back to extr- in the order of least amount of uses to the most amount of uses (A+/B+ ---> O-)
        if have[x] - need[x] >= extraN + extroN + extroP:
          extraP = have[x] - need[x] - extraP - extroN - extroP #Finding how much extraN is left
        elif have[x] - need[x] >= extroN + extroP:
          extraN = have[x] - need[x] - extroN - extroP
          extraP = 0
        elif have[x] - need[x] >= extroN:
          extroP = have[x] - need[x] - extroN
          extraN = 0
          extraP = 0
        else: #If the remaining is greater or equal to zero, but less than the amount of extroP
          extroN = have[x] - need[x] 
          extraN = 0
          extraP = 0
          extroP = 0
      else: #If we still need more even after everything is added (need[x] > have[x])
        result = result + have[x]
        extraN = 0
        extraP = 0
        extroN = 0
        extroP = 0
    elif x == 4: #This is B- and can take B- or O-
      have[x] = have[x] + extroN
      if have[x] >= need[x]:
        extroN = have[x] - need[x]
        result = result + need[x]
      else:
        extroN = 0
        result = result + have[x]
    elif x == 5: #Type: B+, can take B-, B+, O-, O+
      have[x] = have[x] + extrbN + extrbP + extroN + extroP
      if have[x] >= need[x]:
        result = result + need[x]
        if have[x] - need[x] >= extrbN + extroN + extroP:
          extrbP = have[x] - need[x] - extrbP - extroN - extroP 
        elif have[x] - need[x] >= extroN + extroP:
          extrbN = have[x] - need[x] - extroN - extroP
          extrbP = 0
        elif have[x] - need[x] >= extroN:
          extroP = have[x] - need[x] - extroN
          extrbN = 0
          extrbP = 0
        else: 
          extroN = have[x] - need[x] 
          extrbN = 0
          extrbP = 0
          extroP = 0
      else: 
        result = result + have[x]
        extrbN = 0
        extrbP = 0
        extroN = 0
        extroP = 0
    elif x == 6: #This one will be a geezer #Type AB-, will take AB-, A-, B-, O-,
      have[x] = have[x] + extrbN + extraN + extroN
      if have[x] >= need[x]:
        result = result + need[x]
        if have[x] - need[x] >= extrbN + extraN + extroN:
          extrabN = have[x] - need[x] - extrbN - extraN - extroN
        elif have[x] - need[x] >= extraN + extroN:
          extrbN = have[x] - need[x] - extroN - extraN
          extrabN = 0
        elif have[x] - need[x] >= extroN:
          extraN = have[x] - need[x] - extroN
          extrbN = 0
          extrabN = 0
        else: 
          extroN = have[x] - need[x] 
          extraN = 0
          extrbN = 0
          extrabN = 0
      else: 
        result = result + have[x]
        extroN = 0
        extrbN = 0
        extraN = 0
        extrabN = 0
    elif x == 7:
      have[x] = have[x] + extroN + extroP + extraN + extraP + extrbN + extrbP + extrabN + extrabP
      if have[x] >= need[x]:
        result = result + need[x]
      else:
        result = result + have[x]
        
print result
