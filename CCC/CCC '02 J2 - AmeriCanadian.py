looper = True
while looper == True:

  word = raw_input()
  if word == "quit!":
    break
  elif len(word) > 3:
    for x in range(len(word)):
      if word[len(word)-3] != "a" and word[len(word)-3] != "e" and word[len(word)-3] != "i" and word[len(word)-3] != "o" and word[len(word)-3] != "u" and word[len(word)-3] != "y" and word[len(word)-2:len(word)] == "or":
          print word.replace("or","our")
          break
      else:
        print word
        break
  else:
    print word
