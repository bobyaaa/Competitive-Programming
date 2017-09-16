# I ABSOLUTELY HATE PALINDROMESSSSSSSSSSSSSSSSSSSSSSS T_T
# I HATE EM

n = input()
string = raw_input()
options = []
palindrome_length = 0
palindrome_max = 0
palindrome = ""

for x in range(1, n):
  if string[x] == string[x-1]:
    options.append([x, x-1])
  
for x in range(2, n):
  if string[x] == string[x - 2]:
    options.append([x-2, x])

for x in range(len(options)):
  if abs(options[x][1] - options[x][0]) == 1:
    palindrome_length = 0
    for y in range(n):
      if options[x][0] - y < 0 or options[x][1] + y > n - 1:
        break
      else:
        if string[options[x][0] - y] == string[options[x][1] + y]:
          palindrome_length = 2*y 
          if palindrome_length > palindrome_max:
            palindrome = string[(options[x][0]-y):(options[x][1]+y + 1)]
            palindrome_max = palindrome_length
        else:
          break
  else:  
    palindrome_length = 1
    for y in range(n):
      if options[x][0] - y < 0 or options[x][1] + y > n - 1:
        break
      else:
        if string[options[x][0] - y] == string[options[x][1] + y]: 
          palindrome_length = 2*y + 3
          if palindrome_length > palindrome_max:
            palindrome = string[options[x][0]-y:options[x][1]+y + 1]
            palindrome_max = palindrome_length
        else:
          break

print palindrome
print palindrome_max
