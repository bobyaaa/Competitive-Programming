#https://www.quora.com/Given-a-string-how-do-I-find-the-number-of-distinct-substrings-of-the-string
#This guy gives a beautiful explanation ^^^
#Code by Andrew Xing

def longest_common_prefix(suffix1, suffix2):
  LCP = 0
  
  if len(suffix1) > len(suffix2):
    if suffix1.index(suffix2[0]) == 0:
      for x in range(len(suffix2)):
        if suffix1[x] == suffix2[x]:
          LCP = LCP + 1
        else:
          break
  else:
    if suffix2.index(suffix1[0]) == 0:
      for x in range(len(suffix1)):
        if suffix1[x] == suffix2[x]:
          LCP = LCP + 1
        else:
          break
  
  return LCP
  
n = input()

for i in range(n):
  string = raw_input()
  suffix = []
  for x in range(len(string)):
    suffix.append(string[x:len(string)])
    
  suffix.sort()
  
  result = len(suffix[0])
  for x in range(1, len(suffix)):
    result = result + len(suffix[x]) - longest_common_prefix(suffix[x], suffix[x - 1])
    
  print result + 1
