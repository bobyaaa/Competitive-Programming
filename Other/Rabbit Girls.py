rabbit_girls = input()
group = input()

if group > rabbit_girls:
  print group - rabbit_girls
elif group == rabbit_girls:
  print 0
else:
  remainder = rabbit_girls % group
  if remainder == 0:
    print 0
  elif remainder > float(group/2):
    print group - remainder
  else:
    print remainder
